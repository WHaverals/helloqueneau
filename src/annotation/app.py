import streamlit as st
import time
from datetime import datetime
from pathlib import Path
import pandas as pd
from data_prep import get_story_pairs
from start_page import show_landing_page
from styles import load_css

def save_responses_to_file(responses, session_id=None):
    """Save responses to a CSV file using session ID"""
    save_dir = Path("responses")
    save_dir.mkdir(exist_ok=True)
    
    # Use session_id for the filename if provided, otherwise create new session_id
    if session_id is None:
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Use a consistent filename throughout the session
    filepath = save_dir / f"responses_session_{session_id}.csv"
    
    # Save to CSV
    pd.DataFrame(responses).to_csv(filepath, index=False)
    return filepath

def create_annotation_app(story_pairs):
   st.markdown(load_css(), unsafe_allow_html=True)

   # Initialize session state
   if 'session_id' not in st.session_state:
       st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
       
   if 'current_pair_index' not in st.session_state:
       st.session_state.current_pair_index = 0
       st.session_state.responses = []
       st.session_state.start_time = datetime.now()
       st.session_state.pair_start_time = time.time()
       st.session_state.selected_style_1 = None
       st.session_state.selected_style_2 = None
       st.session_state.completed = False

   # Show completion page if experiment is done
   if st.session_state.completed:
       st.success("Task completed! Thank you for your participation.")
       results_df = pd.DataFrame(st.session_state.responses)
       st.download_button(
           label="Download Final Results",
           data=results_df.to_csv(index=False),
           file_name=f"annotation_results_session_{st.session_state.session_id}.csv",
           mime="text/csv"
       )
       return

   # Ensure current_pair_index is valid
   total_pairs = len(story_pairs)
   if st.session_state.current_pair_index >= total_pairs:
       st.session_state.current_pair_index = 0

   current_index = st.session_state.current_pair_index
   progress = current_index / total_pairs
   
   # Get current pair
   current_pair = story_pairs[current_index]
   labels = current_pair['labels']
   
   with st.sidebar:
       st.progress(progress)
       st.write(f"Progress: {current_index}/{total_pairs} pairs completed")
       st.markdown("#### Instructions")
       st.write("1. Read both stories carefully")
       st.write("2. Select the appropriate style for each story")
       st.write("3. Rate your confidence in your classifications")
       st.write("4. Click 'Submit and Continue' to move to the next pair")

   # Display stories side by side
   col1, col2 = st.columns(2)
   with col1:
       st.markdown("""<div class="style-header">Select a style label for<span>Story 1</span></div>""", unsafe_allow_html=True)
       button_cols1 = st.columns(len(labels))
       
       for idx, label in enumerate(labels):
           button_clicked = button_cols1[idx].button(
               label,
               key=f"story1_{label}",
               type=("primary" if st.session_state.selected_style_1 == label else "secondary"),
               use_container_width=True
           )
           
           if button_clicked:
               st.session_state.selected_style_1 = label
               # Auto-select the opposite label for Story 2
               st.session_state.selected_style_2 = [l for l in labels if l != label][0]
               st.rerun()

       st.code(current_pair['story1']['text'], language="markdown", wrap_lines=True)  # language=None for plain text
   
   with col2:
       st.markdown("""<div class="style-header">Select a style label for<span>Story 2</span></div>""", unsafe_allow_html=True)
       button_cols2 = st.columns(len(labels))
       for idx, label in enumerate(labels):
           button_clicked = button_cols2[idx].button(
               label,
               key=f"story2_{label}",
               type=("primary" if st.session_state.selected_style_2 == label else "secondary"),
               use_container_width=True
           )
           
           if button_clicked:
               st.session_state.selected_style_2 = label
               # Auto-select the opposite label for Story 1
               st.session_state.selected_style_1 = [l for l in labels if l != label][0]
               st.rerun()

       st.code(current_pair['story2']['text'], language="markdown", wrap_lines=True)  # language=None for plain text
   
   st.divider()    
   # Confidence rating section
   st.write("### Rate your confidence in this classification")
   
   confidence_options = [
       "Not at all confident",
       "Slightly confident", 
       "Moderately confident",
       "Very confident",
       "Extremely confident"
   ]

   # Create columns for the confidence buttons
   conf_cols = st.columns(5)
   
   # Store the selected confidence in session state if not already there
   if 'selected_confidence' not in st.session_state:
       st.session_state.selected_confidence = None
   
   # Create a button for each confidence level
   for idx, (col, option) in enumerate(zip(conf_cols, confidence_options)):
       is_selected = st.session_state.selected_confidence == idx + 1
       if col.button(
           option,
           key=f"conf_{idx}",
           type="primary" if is_selected else "secondary",
           use_container_width=True
       ):
           st.session_state.selected_confidence = idx + 1
           st.rerun()
   
   # Get the confidence value for storage
   confidence = st.session_state.selected_confidence

   # Display timers
   current_time_spent = time.time() - st.session_state.pair_start_time
   total_time = datetime.now() - st.session_state.start_time
   st.session_state.current_time_spent = round(current_time_spent, 1)
   st.session_state.total_time = str(total_time).split('.')[0]

   # Update submit button condition
   submit_disabled = not (st.session_state.selected_style_1 and 
                       st.session_state.selected_style_2 and 
                       confidence)  # Add confidence check
   st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
   if st.button("Submit and Continue", disabled=submit_disabled, type="primary", use_container_width=True, key="submit"):
       # Calculate time spent on this pair
       time_spent = time.time() - st.session_state.pair_start_time
       
       # Store response using session state variables
       response = {
           'pair_id': current_pair['pair_id'],
           'difficulty': current_pair['difficulty'],
           'story1_true_label': current_pair['story1']['label'],
           'story2_true_label': current_pair['story2']['label'],
           'story1_selected_label': st.session_state.selected_style_1,
           'story2_selected_label': st.session_state.selected_style_2,
           'confidence_rating': confidence,
           'time_spent_seconds': round(time_spent, 2),
           'timestamp': datetime.now().isoformat()
       }
       st.session_state.responses.append(response)

       # Save after each submission using session_id
       try:
           save_filepath = save_responses_to_file(
               st.session_state.responses, 
               st.session_state.session_id
           )
           st.toast(f"Progress saved", icon="✅")
       except Exception as e:
           st.warning(f"Could not save progress: {str(e)}")

       # Reset selections and move to next pair
       if current_index < total_pairs - 1:
           st.session_state.current_pair_index += 1
           st.session_state.pair_start_time = time.time()
           st.session_state.selected_style_1 = None
           st.session_state.selected_style_2 = None
           st.session_state.selected_confidence = None
           st.rerun()
       else:
           st.session_state.completed = True
           st.rerun()

def main():
    # Set page config to collapse sidebar by default
    st.set_page_config(
        initial_sidebar_state="collapsed",
        page_title="Style Classification",
        layout="wide"
    )
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = "landing"

    # Show appropriate page
    if st.session_state.page == "landing":
        if show_landing_page():  # If button is clicked
            st.session_state.page = "experiment"
            st.rerun()
    else:
        story_pairs = get_story_pairs()
        create_annotation_app(story_pairs)

if __name__ == "__main__":
    main()