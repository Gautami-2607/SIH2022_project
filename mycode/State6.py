from tkinter.messagebox import showwarning #DONE 2
from numpy import sort                     
import pandas as pd
import plotly.express as px
import streamlit as st

"""st.set_page_config(page_title="State wise Student Dashboard",
                   page_icon=":blue_book:",
                   layout = "wide"
                   )
"""
def state():
    @st.cache
    def get_data_from_excel():
        df = pd.read_excel("Student_Data_4.xlsx")
        df = df.fillna(0)
        return df
    # now when we run we can see page title, page name, page icon


    df = get_data_from_excel()
    ###########st.dataframe(df)

    st.sidebar.header("Select the Credentials here")

    year = st.sidebar.selectbox("Select the Year: ", options= df["Year"].unique())

    state_id = st.sidebar.selectbox(
        "Select state from below: ",
        options = sort(df["State_ID"].unique()),
    )
    def getdistricts(l):
        dist=[]
        for j in l:
            for i in range(110):
                if(df.loc[i,"State_ID"]==j):
                    dist.append(df.loc[i,"District_ID"])
                    continue
                else:
                    pass
        return list(set(dist))

    district_id = st.sidebar.multiselect(
        "Select the Districts:",#label
        #options = sort(df["District_ID"].unique()),
        options = getdistricts([state_id])
    )

    def getschools(l):
        schools=[]
        for j in l:
            for i in range(110):
                if(df.loc[i, "District_ID"]==j):
                    schools.append(df.loc[i, "School_ID"])
                    continue
                else:
                    pass
        return list(set(schools))


    def getstudents(l):
        students=[]
        for j in l:
            for i in range(110):
                if(df.loc[i,"School_ID"]==j):
                    students.append(df.loc[i,"Student_ID"])
                else:
                    pass
        return students
    #schools= st.sidebar.multiselect("Select the school:",options=getschools(district_id))


    gender = st.sidebar.multiselect(
        "Select the Gender:",# label
        options = ["Male", "Female", "Others"],
        default = ["Male", "Female","Others"]
    )


    df_selection = df.query(
        "State_ID == @state_id & District_ID == @district_id & Gender == @gender & Year ==@year"
    )
    df_selection2 = df.query(
        "State_ID == @state_id & Gender == @gender & Year ==@year"
    )
    df_selection3 = df.query(
        "District_ID==@district_id & Gender == @gender & Year ==@year"
    )



    #--MAIN PAGE--
    st.title(":blue_book: State Dashboard")
    st.markdown("##")# inserting paragraph here to seperate title from KPI's
    #st.markdown("""<h2>The state wise statistics of student results</h2>""", unsafe_allow_html = True)



    #########################################
    # TOP KPI's
    #st.markdown("---")


    ###

    md=df_selection2.groupby(['District_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
    md1 = md["Final_Result"].mean()
    e=st.sidebar.number_input("Select the criteria",min_value=5.0,max_value=df_selection["Final_Result"].max(),value=md["Final_Result"].mean())



    st.markdown("""<h3> State-Level Analysis </h3>""", unsafe_allow_html=True)

    Final_District_Analysis = df_selection2.groupby(['District_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")

    import plotly.graph_objects as go
    p = df_selection2.groupby('District_ID').mean()[["Final_Result"]]
    x = p.index
    y = p["Final_Result"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    color_discrete_sequence =['#000080']*3
    fig.update_traces(marker_color='#000080')
    if (md1>=5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1= md1, xref="paper",
                  y0= md1, y1= md1, yref="y")
    fig.add_annotation(x=df["District_ID"], y=Final_District_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='Target')
    #fig.show()
    st.plotly_chart(fig)

    ##############################################
    st.markdown("---")
    st.markdown("""<h3>Analysis Among Desired Districts  </h3>""", unsafe_allow_html=True)
    Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")

    import plotly.graph_objects as go
    p = df_selection.groupby('District_ID').mean()[["Final_Result"]]
    x = p.index
    y = p["Final_Result"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    color_discrete_sequence =['#000080']*3
    fig.update_traces(marker_color='#000080')
    if(e>=5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1= e , xref="paper",
                 y0= e , y1= e , yref="y")
    fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='')
    #fig.show()
    st.plotly_chart(fig)

    ##############################
    st.markdown("---")
    st.markdown("""<h3>Analysis Among Schools  </h3>""", unsafe_allow_html=True)
    Final_School_Analysis = df_selection.groupby(['School_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")


    import plotly.graph_objects as go
    p = df_selection.groupby('School_ID').mean()[["Final_Result"]]
    x = p.index
    y = p["Final_Result"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    color_discrete_sequence =['#000080']*3
    fig.update_traces(marker_color='#000080')
    if(e>=5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
    fig.add_annotation(x=df["School_ID"], y=Final_School_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=0 ,text='')
    #fig.show()
    st.plotly_chart(fig)
    st.markdown("---")


    #st.markdown(hide_st_style, unsafe_allow_html= True)
    st.markdown("""<h3>Brief View on Individual Achivement of Nipun Bharat LAKSHYAS</h3>""",unsafe_allow_html=True)

    ##

    skills=st.sidebar.selectbox("Select any skill:",
           options=['Oral','Decoding', 'Reading', 'Writing', 'Speaking',
           'Concept_Understanding', 'Statistics', 'Spatial_Understanding',
           'Measurement', 'Data_Handling']
           )

    ###
    ###


    st.sidebar.text("Choose the visualization technique")
    b=st.sidebar.button("BARGRAPH")
    a=st.sidebar.button("PIECHART")
    if(a):
        #if(clms=="Student"):
        if(skills=="Oral"):
            st.markdown("""<h5> Comparision of Oral Skills </h5>""", unsafe_allow_html=True)
            pc_data= df_selection.groupby(['District_ID']).mean()[['Oral']].sort_values(
            by="Oral")
            pc1 = px.pie(values=pc_data["Oral"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Decoding"):
            st.markdown("""<h5> Comparision of Decoding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Decoding']].sort_values(
                by="Decoding")
            pc1 = px.pie(values=pc_data["Decoding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Reading"):
            st.markdown("""<h5> Comparision of Reading Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Reading']].sort_values(
                by="Reading")
            pc1 = px.pie(values=pc_data["Reading"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Writing"):
            st.markdown("""<h5> Comparision of Writing Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Writing']].sort_values(
                by="Writing")
            pc1 = px.pie(values=pc_data["Writing"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Speaking"):
            st.markdown("""<h5> Comparision of Speaking Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Speaking']].sort_values(
                by="Speaking")
            pc1 = px.pie(values=pc_data["Speaking"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Spatial_Understanding"):
            st.markdown("""<h5> Comparision of Spatial Understanding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Spatial_Understanding']].sort_values(
                by="Spatial_Understanding")
            pc1 = px.pie(values=pc_data["Spatial_Understanding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Measurement"):
            st.markdown("""<h5> Comparision of Measurement Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Measurement']].sort_values(
                by="Measurement")
            pc1 = px.pie(values=pc_data["Measurement"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Data_Handling"):
            st.markdown("""<h5> Comparision of Data Handling Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Data_Handling']].sort_values(
                by="Data_Handling")
            pc1 = px.pie(values=pc_data["Data_Handling"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Concept_Understanding"):
            st.markdown("""<h5> Comparision of Concept Understanding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Concept_Understanding']].sort_values(
                by="Concept_Understanding")
            pc1 = px.pie(values=pc_data["Concept_Understanding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Statistics"):
            st.markdown("""<h5> Comparision of Statistical Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['District_ID']).mean()[['Statistics']].sort_values(
                by="Statistics")
            pc1 = px.pie(values=pc_data["Statistics"],names=pc_data.index)
            st.plotly_chart(pc1)

    if(b):
        if(skills=="Oral"):
            st.markdown("""<h5> Comparision of Oral Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Oral']].sort_values(by="Oral")
            p = df_selection.groupby('District_ID').mean()[["Oral"]]
            x = p.index
            y = p["Oral"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Oral"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)


        if (skills=="Decoding"):
            st.markdown("""<h5> Comparision of Decoding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Decoding']].sort_values(by="Decoding")
            p = df_selection.groupby('District_ID').mean()[["Decoding"]]
            x = p.index
            y = p["Decoding"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Decoding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Reading"):
            st.markdown("""<h5> Comparision of Reading Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Reading']].sort_values(by="Reading")
            p = df_selection.groupby('District_ID').mean()[["Reading"]]
            x = p.index
            y = p["Reading"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Reading"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Writing"):
            st.markdown("""<h5> Comparision of Writing Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Writing']].sort_values(by="Writing")
            p = df_selection.groupby('District_ID').mean()[["Writing"]]
            x = p.index
            y = p["Writing"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Writing"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Speaking"):
            st.markdown("""<h5> Comparision of Speaking Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Speaking']].sort_values(by="Speaking")
            p = df_selection.groupby('District_ID').mean()[["Speaking"]]
            x = p.index
            y = p["Speaking"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Speaking"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Concept_Understanding"):
            st.markdown("""<h5> Comparision of Concept Understanding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Concept_Understanding']].sort_values(by="Concept_Understanding")
            p = df_selection.groupby('District_ID').mean()[["Concept_Understanding"]]
            x = p.index
            y = p["Concept_Understanding"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Concept_Understanding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Spatial_Understanding"):
            st.markdown("""<h5> Comparision of Spatial Understanding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Spatial_Understanding']].sort_values(by="Spatial_Understanding")
            p = df_selection.groupby('District_ID').mean()[["Spatial_Understanding"]]
            x = p.index
            y = p["Spatial_Understanding"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Spatial_Understanding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Statistics"):
            st.markdown("""<h5> Comparision of Statistical Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Statistics']].sort_values(by="Statistics")
            p = df_selection.groupby('District_ID').mean()[["Statistics"]]
            x = p.index
            y = p["Statistics"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Statistics"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Measurement"):
            st.markdown("""<h5> Comparision of Measurement Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Measurement']].sort_values(by="Measurement")
            p = df_selection.groupby('District_ID').mean()[["Measurement"]]
            x = p.index
            y = p["Measurement"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Measurement"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Data_Handling"):
            st.markdown("""<h5> Comparision of Data Handling Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['District_ID']).mean()[['Data_Handling']].sort_values(by="Data_Handling")
            p = df_selection.groupby('District_ID').mean()[["Data_Handling"]]
            x = p.index
            y = p["Data_Handling"]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=x, y=y))
            fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
            color_discrete_sequence =['#000080']*3
            fig.update_traces(marker_color='#000080')
            if(e>=5):
                fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
            fig.add_annotation(x=df["District_ID"], y=Final_Student_Analysis["Data_Handling"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
     header {visibility: hidden;}
     </style>
     """
    st.markdown(hide_st_style, unsafe_allow_html= True)