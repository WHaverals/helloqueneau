def load_css():
    return """
        <style>
        /* Container sizing */
        .block-container {
            max-width: 95% !important;
            padding-top: 5rem !important;
        }
        
        /* Style selection headers */
        .style-header {
            text-align: center;
            font-size: 1.2rem;
            margin: 1.5rem 0;
            line-height: 1.6;
        }
        
        .style-header span {
            display: block;
            font-weight: bold;
            margin-top: 0.5rem;
        }
        
        /* Story columns */
        [data-testid="column"] {
            padding: 1rem;
        }
        
        /* Story text areas */
        .stTextArea textarea {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1rem;
            background: #ffffff;
            margin-top: 1rem;
        }
        
        /* Base button styling - for story and confidence buttons */
        .stButton > button:not([key="submit"]) {  /* Everything EXCEPT submit button */
            width: 100% !important;
            padding: 0.5rem !important;
            border: 1px solid #ddd !important;
            background-color: white !important;
            color: #31333F !important;
            transition: all 0.2s ease !important;
        }

        /* Selected button state - for story and confidence buttons */
        .stButton > button:not([key="submit"])[kind="primary"] {
            background-color: #e7f0ff !important;
            border-color: #007bff !important;
            color: #007bff !important;
        }

        /* Button hover - for story and confidence buttons */
        .stButton > button:not([key="submit"]):hover {
            border-color: #007bff !important;
            background-color: #f8f9fa !important;
        }

        /* Submit button - enabled state (when choices are made) */
        .stButton > button[key="submit"]:not([disabled]) {
            background-color: #0056b3 !important;     /* Darker blue background */
            border: 1px solid #004494 !important;     /* Slightly darker border */
            color: white !important;                  /* White text */
            font-weight: 500 !important;             
            padding: 0.75rem !important;              
            margin-top: 2rem !important;              
            border-radius: 6px !important;            
        }

        /* Submit button hover */
        .stButton > button[key="submit"]:not([disabled]):hover {
            background-color: #004494 !important;     /* Even darker blue on hover */
            border-color: #003673 !important;         
        }

        /* Submit button disabled */
        .stButton > button[key="submit"][disabled] {
            background-color: #e9ecef !important;     /* Light gray when disabled */
            border-color: #dee2e6 !important;
            color: #adb5bd !important;
        }
        
        /* Hide timer info */
        [data-testid="stText"]:has(> div:contains("Time spent")) {
            display: none;
        }
        
        /* Confidence section and header */
        [data-testid="stMarkdown"] h3 {
            text-align: center;
            margin: 2rem 0;
        }
        
        /* Confidence buttons styling */
        div[data-testid="column"] .stButton > button {
            white-space: normal !important;
            height: auto !important;
            min-height: 45px !important;
            padding: 0.5rem !important;
            font-size: 0.9rem !important;
            line-height: 1.2 !important;
        }
        
        /* Selected confidence button state */
        div[data-testid="column"] .stButton > button[kind="primary"] {
            background-color: #e7f0ff !important;
            border-color: #007bff !important;
            color: #007bff !important;
            box-shadow: 0 0 0 1px rgba(0,123,255,0.3) !important;
            font-weight: 600 !important;
        }

        /* Confidence button hover */
        div[data-testid="column"] .stButton > button:hover {
            border-color: #007bff !important;
            background-color: #f8f9fa !important;
        }

        </style>
    """