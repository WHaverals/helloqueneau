# start_page.py
import streamlit as st
from styles import load_css

def show_landing_page():
    # Center the logo using container_width
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.image("logo.png", use_container_width=True)
    
    # Just the subtitle since logo contains the main title
    st.markdown("""
        <div style='text-align: center;'>
            <h3 style='color: #666; margin: 1rem 0 2rem 0;'>Style Classification Annotation Task</h3>
        </div>
    """, unsafe_allow_html=True)

    # Add some spacing before the welcome heading
    st.write("")  # Adds vertical space
    
    # Welcome section with improved formatting
    st.markdown("### Welcome to the Style Classification Experiment")
    
    # Main description with better line height
    st.markdown("""
        <p style='font-size: 1.1em; line-height: 1.6; margin-bottom: 2rem;'>
            In this experiment, you will be shown pairs of stories and asked to classify their styles. 
            Each story is a different retelling of the same basic narrative.
        </p>
    """, unsafe_allow_html=True)
    
    # Task overview with better spacing
    st.markdown("#### Task Overview")
    task_list = """
    1. Read both stories carefully
    2. Select the appropriate style for each story
    3. Rate your confidence in your classifications
    4. Click 'Submit and Continue' to move to the next pair
    """
    st.markdown(task_list)
    
    # Add spacing before important information
    st.write("")
    
    # Important information in a container for visual grouping
    with st.container():
        st.markdown("#### Important Information")
        cols = st.columns(2)
        
        with cols[0]:
            st.markdown("- Total number of pairs: 49")
            st.markdown("- Estimated time per pair: 2-3 minutes")
            st.markdown("- Total estimated time: 2 hours")
        
        with cols[1]:
            st.markdown("- You can take breaks between pairs")
            st.markdown("- Your progress is saved automatically")

    # Add spacing before button
    st.write("")
    st.write("")
    
    # Center the start button with more generous spacing
    _, button_col, _ = st.columns([1, 1.2, 1])
    with button_col:
        return st.button(
            "Start Experiment",
            type="primary",
            use_container_width=True
        )