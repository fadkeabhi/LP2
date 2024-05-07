import streamlit as st
from typing import Dict, List

mental_health_knowledge_base: Dict[str, List[str]] = {
    "Depression": [
        "feeling sad or having a depressed mood",
        "loss of interest or pleasure in activities once enjoyed",
        "changes in appetite — weight loss or gain unrelated to dieting",
        "trouble sleeping or sleeping too much",
        "loss of energy or increased fatigue",
        "feeling worthless or guilty",
        "trouble thinking, concentrating, or making decisions",
        "thoughts of death or suicide",
    ],
    "Anxiety": [
        "feeling nervous, restless or tense",
        "having a sense of impending danger, panic or doom",
        "increased heart rate",
        "rapid breathing (hyperventilation)",
        "sweating",
        "trembling",
        "feeling weak or tired",
        "difficulty concentrating or thinking about anything other than the present worry",
    ],
    "Stress": [
        "feeling overwhelmed or unable to cope",
        "irritability or moodiness",
        "feeling anxious or worried",
        "low energy or fatigue",
        "difficulty sleeping",
        "difficulty concentrating",
        "rapid heartbeat or chest pains",
        "headaches or muscle tension",
    ],
}

st.header("Mental Health Expert System")

def respond(input: List[str]):
    symptoms = input
    if len(symptoms) == 0:
        return

    if any(symptoms[0] != symptom[0] for symptom in mental_health_knowledge_base.values() for _ in range(len(symptom))):
        st.write("Question is not present in the knowledge base!")
        st.write("Could you please enter the appropriate answer for the question below-")
        answer = st.text_input("Answer")
        add = st.button("Add answer")
        if add:
            for key in mental_health_knowledge_base:
                if symptoms[0] == key:
                    mental_health_knowledge_base[key].append(answer)
    else:
        for condition, symptoms_list in mental_health_knowledge_base.items():
            if all(symptoms[0] in symptoms_list):
                st.write(f"You may have {condition}.")
                st.write("Please consider consulting a mental health professional for further evaluation and treatment.")

if __name__ == "__main__":
    symptoms = st.multiselect(
        'Which symptoms are you experiencing?',
        [
            "feeling sad or having a depressed mood",
            "loss of interest or pleasure in activities once enjoyed",
            "changes in appetite — weight loss or gain unrelated to dieting",
            "trouble sleeping or sleeping too much",
            "loss of energy or increased fatigue",
            "feeling worthless or guilty",
            "trouble thinking, concentrating, or making decisions",
            "thoughts of death or suicide",
            "feeling nervous, restless or tense",
            "having a sense of impending danger, panic or doom",
            "increased heart rate",
            "rapid breathing (hyperventilation)",
            "sweating",
            "trembling",
            "feeling weak or tired",
            "difficulty concentrating or thinking about anything other than the present worry",
            "feeling overwhelmed or unable to cope",
            "irritability or moodiness",
            "feeling anxious or worried",
            "low energy or fatigue",
            "difficulty sleeping",
            "difficulty concentrating",
            "rapid heartbeat or chest pains",
            "headaches or muscle tension",
        ],
    )

    col1, col2 = st.columns([1, 0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if ask:
        respond(symptoms)
    if quit:
        st.write("Thank youfor using the Mental Health Expert System!")