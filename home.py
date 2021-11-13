import streamlit as st
from PIL import Image
from styling import footer


def app():

    st.error("finish the help part")
    st.markdown("# Welcome To 'WeGotYou' ")
    st.text("no matter what you feel,it's genuine...")
    "\n"
    st.subheader("A Brief Overview")
    st.write(" In recent years, there has been increasing acknowledgement of the important role mental health plays in achieving global development goals, as illustrated by the inclusion of mental health in the Sustainable Development Goals. Depression is one of the leading causes of disability. \n\n Suicide is the second leading cause of death among 15-29-year-olds. People with severe mental health conditions die prematurely – as much as two decades early – due to preventable physical conditions. \n Despite progress in some countries, people with mental health conditions often experience severe human rights violations, discrimination, and stigma. \n\n Many mental health conditions can be effectively treated at relatively low cost, yet the gap between people needing care and those with access to care remains substantial. Effective treatment coverage remains extremely low. \n\n Mental illnesses affect 19 % of the adult population, 46 % of teenagers and 13 % of children each year. People struggling with their mental health may be in your family, live next door, teach your children, work in the next cubicle or sit in the same church pew.\n\n However, only half of those affected receive treatment, often because of the stigma attached to mental health. Untreated, mental illness can contribute to higher medical expenses, poorer performance at school and work, fewer employment opportunities and increased risk of suicide.")
    "\n"
    st.header("What Exactly is a Mental Illness!")

    st.write("A mental illness is a physical illness of the brain that causes disturbances in thinking, behavior, energy or emotion that make it difficult to cope with the ordinary demands of life.\n\n &#11089; Research is starting to uncover the complicated causes of these diseases which can include genetics, brain chemistry, brain structure, experiencing trauma and/or having another medical condition, like heart disease.")
    "\n"
    st.subheader("The two most common mental health conditions are:")
    st.write("&#11090; Anxiety Disorders –More than 18% of adults each year struggle with some type of anxiety disorder, including post-traumatic stress disorder (PTSD), obsessive-compulsive disorder (OCD), panic disorder (panic attacks), generalized anxiety disorder and specific phobias.")
    st.write("&#11090; Mood Disorders – Mood disorders, such as depression and bipolar depression, affect nearly 10% of adults each year and are characterized by difficulties in regulating one’s mood.")

    st.subheader("What You Can Do to Help?")
    st.write("Although the general perception of mental illness has improved over the past decades, studies show that stigma against mental illness is still powerful, largely due to media stereotypes and lack of education, and that people tend to attach negative stigmas to mental health conditions at a far higher rate than to other diseases and disabilities, such as cancer, diabetes or heart disease.\n\nStigma affects not only the number seeking treatment, but also the number of resources available for proper treatment. Stigma and misinformation can feel like overwhelming obstacles for someone who is struggling with a mental health condition. Here a few powerful things you can do to help: \n\n")
    st.write("&#11089; Showing individuals respect and acceptance removes a significant barrier to successfully coping with their illness.")
    st.write("&#11089;  Having people see you as an individual and not as your illness can make the biggest difference for someone who is struggling with their mental health.")
    st.write("&#11089; Advocating within our circles of influence helps ensure these individuals have the same rights and opportunities as other members of your church, school and community.")
    st.write("&#11089; Learning more about mental health allows us to provide helpful support to those affected in our families and communities.")
    "\n"
    footer()
app()