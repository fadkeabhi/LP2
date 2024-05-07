import streamlit as st

gardening_knowledge_base = {"Vegetables": ["Tomatoes", "Carrots", "Lettuce", "Bell Peppers", "Zucchini", "Cucumbers", "Spinach",], 
                            "Flowers": ["Roses", "Tulips", "Daisies", "Lilies", "Sunflowers", "Marigolds", "Pansies",], 
                            "Herbs": ["Basil", "Mint", "Parsley", "Rosemary", "Thyme", "Chives", "Cilantro",],}


st.header("Gardening Expert System")

def respond(plant_type):
    if plant_type:
        if plant_type in gardening_knowledge_base.keys():
            st.write(f"Popular {plant_type} to grow:")
            for plant in gardening_knowledge_base[plant_type]:
                st.write("- ", plant)
        else:
            st.write("Plant type is not present in the knowledge base!")
            st.write("Could you please select the appropriate plant type below-")

if __name__ == "__main__":
    plant_type = st.selectbox(
        'What type of plants are you interested in?',
        list(gardening_knowledge_base.keys())
        )

    col1, col2 = st.columns([1, 0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if ask:
        respond(plant_type)
    if quit:
        st.write("Thank you for using the Gardening Expert System!")
