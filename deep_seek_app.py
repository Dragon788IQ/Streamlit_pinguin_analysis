import streamlit as st

def main():
    # Configure page settings
    # st.set_page_config(
    #     page_title="John Doe - Curriculum Vitae",
    #     page_icon="📄",
    #     layout="wide"
    # )

    # Sidebar for contact information
    with st.sidebar:
        st.title("Contact Information")
        st.write("📧 john.doe@email.com")
        st.write("📱 +1 234 567 890")
        st.write("📍 New York, USA")
        st.write("🔗 [LinkedIn](https://linkedin.com/in/johndoe)")
        st.write("💻 [GitHub](https://github.com/johndoe)")
        st.write("📚 [Portfolio](https://johndoeportfolio.com)")

    # Main content
    st.header("John Doe")
    st.subheader("Senior Software Engineer")

    # Professional Summary
    with st.container():
        st.markdown("""
        ### Professional Summary
        Experienced software engineer with 8+ years of expertise in full-stack development, 
        cloud computing, and team leadership. Specialized in building scalable web applications 
        and implementing DevOps practices. Strong background in Python, JavaScript, and AWS.
        """)
        st.markdown("---")

    # Work Experience
    with st.container():
        st.subheader("Work Experience")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Senior Software Engineer**  \n*Tech Corp Inc.*")
            st.markdown("""
            - Led team of 10 developers in building enterprise SaaS platform
            - Implemented CI/CD pipelines reducing deployment time by 40%
            - Developed microservices architecture using AWS Lambda and API Gateway
            """)
        with col2:
            st.markdown("*June 2019 - Present*  \nNew York, USA")

        st.markdown("---")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Software Engineer**  \n*Innovative Solutions Ltd.*")
            st.markdown("""
            - Developed full-stack web applications using React and Node.js
            - Optimized database queries improving application performance by 25%
            - Integrated third-party APIs including payment gateways and SMS services
            """)
        with col2:
            st.markdown("*Jan 2016 - May 2019*  \nLondon, UK")

    # Education
    with st.container():
        st.subheader("Education")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**MSc Computer Science**  \n*University of Technology*")
            st.markdown("- GPA: 3.8/4.0  \n- Thesis: Machine Learning in Cloud Environments")
        with col2:
            st.markdown("*2014 - 2016*  \nLondon, UK")

    # Skills
    with st.container():
        st.subheader("Technical Skills")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **Programming Languages**
            - Python
            - JavaScript
            - Java
            - SQL
            """)
        with col2:
            st.markdown("""
            **Frameworks & Tools**
            - React
            - Node.js
            - Docker
            - AWS
            """)
        with col3:
            st.markdown("""
            **Certifications**
            - AWS Certified Developer
            - Google Cloud Professional
            - Scrum Master Certification
            """)

    # Projects
    with st.container():
        st.subheader("Key Projects")
        with st.expander("E-commerce Platform (2022)"):
            st.markdown("""
            - Built scalable e-commerce platform using microservices architecture
            - Technologies: Python, Django, React, PostgreSQL, Redis
            - Features: Payment processing, recommendation engine, analytics dashboard
            """)
        
        with st.expander("AI Chatbot (2021)"):
            st.markdown("""
            - Developed NLP-powered customer service chatbot
            - Technologies: Python, TensorFlow, Flask, AWS Lambda
            - Achieved 85% customer query resolution rate
            """)

    # Contact Form
    with st.container():
        st.markdown("---")
        st.subheader("Contact Me")
        with st.form(key='contact_form'):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Send Message")
            
            if submit_button:
                # Add your email sending logic here
                st.success("Thank you for your message! I'll respond shortly.")

# Custom CSS styling
st.markdown("""
<style>
    }
    .stContainer {
        padding: 20px;
    }
    .stExpander {
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()