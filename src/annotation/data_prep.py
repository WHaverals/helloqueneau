import pandas as pd
from typing import List, Dict
import config
import streamlit as st

@st.cache_data  # Add caching decorator
def load_and_clean_data(url: str) -> pd.DataFrame:
    """Load and clean the stories dataset."""
    df = pd.read_csv(url)
    eng_df = df[df['lang'] == 'eng'].copy()
    needed_cols = ['id', 'auth', 'story', 'label']
    eng_df = eng_df[needed_cols]
    return eng_df

def create_specific_pairs(df: pd.DataFrame, pair_definitions: List[Dict]) -> List[Dict]:
    """Create specific pairs of stories based on their labels with metadata."""
    pairs = []
    
    for pair_def in pair_definitions:
        story1 = df[df['label'] == pair_def['label1']].iloc[0]
        story2 = df[df['label'] == pair_def['label2']].iloc[0]
        
        pair = {
            'pair_id': pair_def['id'],
            'difficulty': pair_def['difficulty'],
            'story1': {
                'text': story1['story'],
                'label': story1['label']
            },
            'story2': {
                'text': story2['story'],
                'label': story2['label']
            },
            'labels': [pair_def['label1'], pair_def['label2']]
        }
        pairs.append(pair)
    
    return pairs

@st.cache_data
def get_story_pairs():
    """Get prepared story pairs for the annotation task."""
    url = f"https://docs.google.com/spreadsheets/d/{config.sheet_id}/export?format=csv"
    df = load_and_clean_data(url)
    from utils.pair_definitions import desired_pairs
    return create_specific_pairs(df, desired_pairs)