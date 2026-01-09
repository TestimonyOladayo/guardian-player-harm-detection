import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from matplotlib.ticker import ScalarFormatter

# --- 1. BEHAVIORAL DATA ARCHITECTURE ---
def generate_behavioral_data():
    """Simulates 24 hours of player data showing a loss-chasing spiral."""
    np.random.seed(42)
    start_time = datetime(2026, 1, 9, 0, 0)
    timestamps = [start_time + timedelta(minutes=30*i) for i in range(48)]
    
    # Behavioral Logic: Steady Play -> Aggressive Escalation -> Crisis Spiral
    bets = np.concatenate([
        np.random.normal(15, 5, 24),    # Hours 0-12: Normal
        np.random.normal(150, 50, 12),  # Hours 12-18: High Risk
        np.random.normal(1500, 400, 12) # Hours 18-24: Critical Spiral
    ])
    
    df = pd.DataFrame({'Timestamp': timestamps, 'Bet_Size': np.abs(bets)})
    # Calculate Risk Velocity (Moving Average of wagers)
    df['Risk_Velocity'] = df['Bet_Size'].rolling(window=4).mean()
    return df

# --- 2. FORENSIC VISUALIZATION ENGINE ---
def render_guardian_dashboard(df):
    """Renders the professional risk velocity dashboard."""
    plt.figure(figsize=(16, 10), dpi=300)
    
    # Apply Logarithmic Scale for visibility of both $15 and $2000 bets
    plt.yscale('log') 
    
    # Risk Heatmap Background (RdYlGn reversed: Green to Red)
    risk_matrix = df['Risk_Velocity'].values.reshape(1, -1)
    plt.imshow(risk_matrix, aspect='auto', cmap='RdYlGn_r', alpha=0.3,
               extent=[0, 24, df['Bet_Size'].min(), df['Bet_Size'].max() + 2000])

    # Plot Player Journey
    hours = np.linspace(0, 24, len(df))
    plt.plot(hours, df['Bet_Size'], color='#1a1a1a', linewidth=3, marker='o', 
             markersize=8, label='Player Activity')
    
    # Define Intervention Zone
    plt.axvspan(18, 24, color='red', alpha=0.15)
    
    # Professional Annotations
    plt.annotate('BASELINE ACTIVITY', xy=(2, 12), fontsize=12, fontweight='bold', color='#1e5631')
    plt.annotate('RISK ESCALATION', xy=(12.5, 200), fontsize=12, fontweight='bold', color='#cc7a00')
    plt.annotate('CRITICAL SPIRAL: INTERVENTION REQUIRED', xy=(15.5, 1800), 
                 fontsize=15, fontweight='bold', color='#b30000')

    # Executive Title (No Project Name)
    plt.title("PREDICTIVE PLAYER HARM DETECTION: 24-HOUR BEHAVIORAL RISK VELOCITY", 
              fontsize=22, fontweight='bold', color='#2c3e50', pad=35)
    
    plt.xlabel("Hours Since Session Start", fontsize=14, labelpad=15)
    plt.ylabel("Wager Size ($)", fontsize=14, labelpad=15)
    plt.grid(True, which="both", ls="-", alpha=0.15)
    
    # Formatting Y-axis for Dollar Readability
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.tick_params(axis='y', which='minor', left=False)
    
    # SAVE AS THE BRANDED FILENAME
    plt.savefig('guardian_player.png', bbox_inches='tight', facecolor='white')
    plt.show()

if __name__ == "__main__":
    player_df = generate_behavioral_data()
    render_guardian_dashboard(player_df)
