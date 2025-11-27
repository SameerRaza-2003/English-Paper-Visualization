import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import networkx as nx

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Pronunciation Analysis", layout="wide")
st.title("Variables Responsible for Sub-standard Pronunciation in Pakistan")
st.markdown(
    """
**Paper:** International Journal of Innovation Sciences and Research, Vol.8, No, 07, pp.1433-1435, July 2019  
**Authors:** Sadeeq Akbar, Imran Khan, Shams ul Islam  

### Overview
This study investigates the factors responsible for poor pronunciation among Pakistani learners of English.  
> "It is aptly understood that input and authentic listening of speaking is the primary need of correct pronunciation, however, learning English as a second language on the ground of L1’s sounds also deforms pronunciation to some extent."
"""
)
st.markdown("---")

# ---------------- DATA ----------------
factors = ['Primary Sounds Unfamiliarity', 'Tertiary Sounds Unfamiliarity',
           'Ignoring Media', 'Not Copying Natives', 'Comparing L1 with L2']
percentages = [43, 21, 14, 13, 9]

# ---------------- FIRST ROW ----------------
col1, col2 = st.columns(2)

# Pie Chart
with col1:
    st.subheader("Pie Chart - Factor Contribution")
    fig1, ax1 = plt.subplots(figsize=(3,3))
    ax1.pie(percentages, labels=factors, autopct='%1.1f%%', startangle=140,
            colors=sns.color_palette('Set3'), wedgeprops=dict(edgecolor='k'))
    ax1.set_title("Contribution of Factors", fontsize=10)
    st.pyplot(fig1)
    
    with st.expander("Details"):
        st.markdown(
            "**What it shows:** Relative contribution of each factor to poor pronunciation.\n\n"
            "**Part of Paper:** Statistical Analysis\n\n"
            "**Full Quote:**\n"
            "From the displayed statistical data, the most responsible factor for the poor pronunciation is Sounds unfamiliarity at Primary level "
            "which is due to negligence of sounds by teachers at grass root level who from the very start are not taught sounds differences "
            "and their proper manner and place of articulation. This factor disturbs students’ pronunciation greatly which is 43% double "
            "than that of Sounds unfamiliarity at tertiary level which is 21%, however this also leaves great impact on the articulation of students’ speaking. "
            "Similarly, ignoring listening and consulting media for correction pronunciation is comparatively lesser than that of sounds unfamiliarity both at tertiary and primary level which is 14%. "
            "Likewise, Not copying Natives is too a considerable factor for affecting pronunciation of Pakistani speakers which is 13% almost equal to that of Ignoring listening to media. "
            "Last but not the least is Comparing L1 sounds with L2 which is 9% the least amount contributing in rough pronunciation of students in Pakistan."
        )

# Bar Chart
with col2:
    st.subheader("Bar Chart - Factor Impact")
    fig2, ax2 = plt.subplots(figsize=(4,3))
    sns.barplot(x=percentages, y=factors, palette='coolwarm', ax=ax2)
    ax2.set_xlabel("Percentage", fontsize=8)
    ax2.set_ylabel("")
    ax2.set_xlim(0,50)
    ax2.set_title("Impact of Factors", fontsize=10)
    ax2.tick_params(labelsize=8)
    st.pyplot(fig2)
    
    with st.expander("Details"):
        st.markdown(
            "**What it shows:** Comparison of percentage impact of each factor.\n\n"
            "**Part of Paper:** Statistical Analysis\n\n"
            "**Full Quote:**\n"
            "Ignoring input from natives and not exposing to media result in coarse pronunciation where speakers cannot satisfy their needs of communication. "
            "Similarly, unawareness of sounds at primary and tertiary level by teachers/instructors leads to unsatisfactory speaking. "
            "Learning English as a second language based on L1 sounds also deforms pronunciation to some extent."
        )

st.markdown("---")

# ---------------- SECOND ROW ----------------
col3, col4 = st.columns(2)

# Radar Chart
with col3:
    st.subheader("Radar Chart - Multi-factor Influence")
    labels=np.array(factors)
    stats=np.array(percentages)
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats=np.concatenate((stats,[stats[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    fig3, ax3 = plt.subplots(figsize=(3.5,3.5), subplot_kw=dict(polar=True))
    ax3.plot(angles, stats, 'o-', linewidth=1.5, color='#FF5733', markersize=4)
    ax3.fill(angles, stats, alpha=0.25, color='#FF5733')
    ax3.set_thetagrids(angles[:-1]*180/np.pi, labels, fontsize=8)
    ax3.set_title("Radar Chart", fontsize=10, y=1.05)
    st.pyplot(fig3)
    
    with st.expander("Details"):
        st.markdown(
            "**What it shows:** Overall comparison of all factors.\n\n"
            "**Part of Paper:** Statistical Analysis\n\n"
            "**Full Quote:**\n"
            "Those who were taught Phonics at initial level were good enough both at manner and place of articulation. "
            "They had a slight issue in stress and intonation pattern which is not judged here, while those who had poor pronunciation had not been taught Phonics "
            "and they could not differentiate between slight identical sounds. As compared to Phones aware students, the unaware were less proficient in pronouncing English words."
        )

# Grouped Bar
with col4:
    st.subheader("Grouped Bar - Level Comparison")
    data = pd.DataFrame({
        'Level': ['Primary', 'Tertiary'],
        'Sounds Unfamiliarity': [43, 21]
    })
    fig4, ax4 = plt.subplots(figsize=(3.5,3))
    data.plot(kind='bar', x='Level', y='Sounds Unfamiliarity',
              color=['#1f77b4','#ff7f0e'], legend=False, ax=ax4)
    ax4.set_ylabel('Percentage', fontsize=8)
    ax4.set_ylim(0,50)
    ax4.set_title("Primary vs Tertiary", fontsize=10)
    ax4.tick_params(axis='x', labelsize=8)
    ax4.tick_params(axis='y', labelsize=8)
    st.pyplot(fig4)
    
    with st.expander("Details"):
        st.markdown(
            "**What it shows:** Difference in pronunciation issues between Primary and Tertiary levels.\n\n"
            "**Part of Paper:** Negligence of Teaching Sounds at Primary Level\n\n"
            "**Full Quote:**\n"
            "Pronunciation at gross root level at the age of three or four years plays important role in speech in the entire life of a speaker. "
            "Most of the times, in cases such as English as a second language the teachers or instructors at initial level in teaching English pronunciation "
            "are least concerned with kids standard utterances while instructing them for the basic units in rhymes where students are easy to gain what is taught to them. "
            "Most importantly, the manner and place of articulation are not usually on right direction which resultantly cause poor pronunciation."
        )

st.markdown("---")

# ---------------- HEATMAP ----------------
st.subheader("Heatmap - Intensity of Factors")
fig5, ax5 = plt.subplots(figsize=(6,0.8))
heat_data = pd.DataFrame([percentages], columns=factors)
sns.heatmap(heat_data, annot=True, fmt="d", cmap="YlGnBu", cbar=True, ax=ax5)
ax5.set_yticks([])
ax5.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
ax5.set_title("Heatmap", fontsize=10)
st.pyplot(fig5)

with st.expander("Details"):
    st.markdown(
        "**What it shows:** Visual intensity of each factor’s contribution.\n\n"
        "**Part of Paper:** Statistical Analysis\n\n"
        "**Full Quote:**\n"
        "From the displayed statistical data, ignoring listening and consulting media, not copying natives, sounds unfamiliarity at tertiary and primary levels, "
        "and comparing L1 with L2 all contribute differently to sub-standard pronunciation in Pakistani learners. "
        "These factors combined affect articulation, stress, and accuracy of English pronunciation."
    )

st.markdown("---")
# ---------------- FLOW DIAGRAM ----------------
st.subheader("Flow of Pronunciation Issues (Visual)")

# Create directed graph
G = nx.DiGraph()
G.add_nodes_from([
    ("Primary Level Negligence", {"color": "#1f77b4"}),
    ("Tertiary Level Unawareness", {"color": "#ff7f0e"}),
    ("Sub-standard Pronunciation", {"color": "#d62728"}),
    ("Poor Communication", {"color": "#2ca02c"})
])
G.add_edges_from([
    ("Primary Level Negligence", "Tertiary Level Unawareness"),
    ("Tertiary Level Unawareness", "Sub-standard Pronunciation"),
    ("Sub-standard Pronunciation", "Poor Communication")
])

# Define vertical positions for nodes (compact)
pos = {
    "Primary Level Negligence": (0,3),
    "Tertiary Level Unawareness": (0,2),
    "Sub-standard Pronunciation": (0,1),
    "Poor Communication": (0,0)
}

# Node colors
colors = [G.nodes[n]['color'] for n in G.nodes()]

# Compact figure
fig6, ax6 = plt.subplots(figsize=(3,4))
nx.draw(
    G, pos, with_labels=True, arrows=True, node_size=1800,
    node_color=colors, font_size=8, font_color='white',
    arrowstyle='-|>', arrowsize=12
)

# Add legend outside the plot (right side)
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#1f77b4', label='Primary Level Negligence'),
    Patch(facecolor='#ff7f0e', label='Tertiary Level Unawareness'),
    Patch(facecolor='#d62728', label='Sub-standard Pronunciation'),
    Patch(facecolor='#2ca02c', label='Poor Communication')
]
ax6.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1,0.5), fontsize=8)

# Remove axes
ax6.axis('off')

st.pyplot(fig6)

with st.expander("Details"):
    st.markdown(
        "**What it shows:** Conceptual flow from early teaching to poor communication.\n\n"
        "**Part of Paper:** Introduction & Negligence at Primary Level\n\n"
        "**Full Quote:**\n"
        "Teachers or instructors at initial level ... are least concerned with kids standard utterances. "
        "Most importantly, the manner and place of articulation are not usually on right direction which resultantly cause poor pronunciation; "
        "for instance the unit BA which is the combination of consonant{b} and vowel{a:} are from the two different classes of sounds "
        "in which one is Bilabial and the other is long vowel sound."
    )
