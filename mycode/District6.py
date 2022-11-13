import pandas as pd                  # DONE 2,3
import plotly_express as px
import streamlit as st
"""st.set_page_config(page_title="District Dashboard",page_icon=":blue_book:",
                   layout="wide")
"""
def district():
    df=pd.read_excel("Student_Data_4.xlsx")

    st.sidebar.header("Select the Credentials here")
    def getschools(l):
        schools = []
        #for j in l:
        for i in range(df.shape[0]):
                if (df.loc[i, "District_ID"] == l):
                    schools.append(df.loc[i, "School_ID"])
                    continue
                else:
                    pass
        return list(set(schools))

    year = st.sidebar.selectbox("Select the Year: ", options= df["Year"].unique())


    districts=st.sidebar.selectbox("Select the district:",
                                 options=(df["District_ID"].unique())
                                 )

    schools=st.sidebar.multiselect("Select the school:",options=getschools(districts))


    gender = st.sidebar.multiselect(
        "Select the Gender:",# label
        options = ["Male", "Female", "Others"],
        default = ["Male", "Female","Others"]
    )


    df_selection=df.query(
        "District_ID==@districts & School_ID==@schools & Gender == @gender & Year ==@year"
    )
    df_selection2 = df.query(
        "District_ID==@districts & Gender == @gender & Year ==@year"
    )

    ##
    #--MAIN PAGE--
    st.title(":blue_book: District Dashboard")
    st.markdown("##")# inserting paragraph here to seperate title from KPI's
    st.write("""Given below are the school-level statistics of student results""")
    st.markdown("""<h3> District-Level Analysis </h3>""", unsafe_allow_html=True)

    Final_School_Analysis = df_selection2.groupby(['School_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")

    md=df_selection2.groupby(['District_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
    md1 = md["Final_Result"].mean()
    e=st.sidebar.number_input("Select the criteria",min_value=5.0,max_value=df_selection["Final_Result"].max(),value=md["Final_Result"].mean())

    import plotly.graph_objects as go
    p = df_selection2.groupby(['School_ID']).mean()[["Final_Result"]]
    x = p.index
    y = p["Final_Result"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    color_discrete_sequence =['#000080']*3
    fig.update_traces(marker_color='#000080')
    if(md1>5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1= md1 , xref="paper",
                 y0= md1 , y1= md1 , yref="y")
    fig.add_annotation(x=df["School_ID"], y=Final_School_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='Target')
    #fig.show()
    st.plotly_chart(fig)

    st.markdown("---")




    st.markdown("""<h3> Analysis Among Desired Schools </h3>""", unsafe_allow_html=True)
    t=df_selection.groupby(['School_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")

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
    if(e>5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
    fig.add_annotation(x=df["School_ID"], y=t["Final_Result"].mean(),showarrow=False, arrowhead=1,text='')
    #fig.show()
    st.plotly_chart(fig)

    st.markdown("---")
    ##

    skills=st.sidebar.selectbox("Select any skill:",
           options=['Oral','Decoding', 'Reading', 'Writing', 'Speaking',
           'Concept_Understanding', 'Statistics', 'Spatial_Understanding',
           'Measurement', 'Data_Handling']
           )

    st.sidebar.text("Choose the visualization technique")

    b=st.sidebar.button("BARGRAPH")
    a=st.sidebar.button("PIECHART")

    st.markdown("""<h3>Brief View on Individual Achivement of Nipun Bharat LAKSHYAS""", unsafe_allow_html=True)


    if(a):
        #if(clms=="Student"):
        if(skills=="Oral"):
            st.markdown("""<h5> Comparision of Oral Skills </h5>""", unsafe_allow_html=True)
            pc_data= df_selection.groupby(['School_ID']).mean()[['Oral']].sort_values(
            by="Oral")
            pc1 = px.pie(values=pc_data["Oral"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Decoding"):
            st.markdown("""<h5> Comparision of Decoding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Decoding']].sort_values(
                by="Decoding")
            pc1 = px.pie(values=pc_data["Decoding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Reading"):
            st.markdown("""<h5> Comparision of Reading Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Reading']].sort_values(
                by="Reading")
            pc1 = px.pie(values=pc_data["Reading"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Writing"):
            st.markdown("""<h5> Comparision of Writing Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Writing']].sort_values(
                by="Writing")
            pc1 = px.pie(values=pc_data["Writing"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Speaking"):
            st.markdown("""<h5> Comparision of Speaking Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Speaking']].sort_values(
                by="Speaking")
            pc1 = px.pie(values=pc_data["Speaking"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Spatial_Understanding"):
            st.markdown("""<h5> Comparision of Spatial Understanding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Spatial_Understanding']].sort_values(
                by="Spatial_Understanding")
            pc1 = px.pie(values=pc_data["Spatial_Understanding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Measurement"):
            st.markdown("""<h5> Comparision of Measurement Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Measurement']].sort_values(
                by="Measurement")
            pc1 = px.pie(values=pc_data["Measurement"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Data_Handling"):
            st.markdown("""<h5> Comparision of Data Handling Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Data_Handling']].sort_values(
                by="Data_Handling")
            pc1 = px.pie(values=pc_data["Data_Handling"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Concept_Understanding"):
            st.markdown("""<h5> Comparision of Concept Understanding Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Concept_Understanding']].sort_values(
                by="Concept_Understanding")
            pc1 = px.pie(values=pc_data["Concept_Understanding"],names=pc_data.index)
            st.plotly_chart(pc1)

        if (skills=="Statistics"):
            st.markdown("""<h5> Comparision of Statistical Skills </h5>""", unsafe_allow_html=True)
            pc_data = df_selection.groupby(['School_ID']).mean()[['Statistics']].sort_values(
                by="Statistics")
            pc1 = px.pie(values=pc_data["Statistics"],names=pc_data.index)
            st.plotly_chart(pc1)

    if(b):
        if(skills=="Oral"):
            st.markdown("""<h5> Comparision of Oral Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Oral']].sort_values(by="Oral")
            p = df_selection.groupby('School_ID').mean()[["Oral"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Oral"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Decoding"):
            st.markdown("""<h5> Comparision of Decoding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Decoding']].sort_values(by="Decoding")
            p = df_selection.groupby('School_ID').mean()[["Decoding"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Decoding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Reading"):
            st.markdown("""<h5> Comparision of Reading Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Reading']].sort_values(by="Reading")
            p = df_selection.groupby('School_ID').mean()[["Reading"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Reading"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Writing"):
            st.markdown("""<h5> Comparision of Writing Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Writing']].sort_values(by="Writing")
            p = df_selection.groupby('School_ID').mean()[["Writing"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Writing"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Speaking"):
            st.markdown("""<h5> Comparision of Speaking Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Speaking']].sort_values(by="Speaking")
            p = df_selection.groupby('School_ID').mean()[["Speaking"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Speaking"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Concept_Understanding"):
            st.markdown("""<h5> Comparision of Concept Understanding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Concept_Understanding']].sort_values(by="Concept_Understanding")
            p = df_selection.groupby('School_ID').mean()[["Concept_Understanding"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Concept_Understanding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Spatial_Understanding"):
            st.markdown("""<h5> Comparision of Spatial Understanding Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Spatial_Understanding']].sort_values(by="Spatial_Understanding")
            p = df_selection.groupby('School_ID').mean()[["Spatial_Understanding"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Spatial_Understanding"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Statistics"):
            st.markdown("""<h5> Comparision of Statistical Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Statistics']].sort_values(by="Statistics")
            p = df_selection.groupby('School_ID').mean()[["Statistics"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Statistics"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Measurement"):
            st.markdown("""<h5> Comparision of Measurement Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Measurement']].sort_values(by="Measurement")
            p = df_selection.groupby('School_ID').mean()[["Measurement"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Measurement"].mean(), showarrow=False, arrowhead=0 ,text='')
            #fig.show()
            st.plotly_chart(fig)

        if (skills=="Data_Handling"):
            st.markdown("""<h5> Comparision of Data Handling Skills </h5>""", unsafe_allow_html=True)
            Final_Student_Analysis = df_selection.groupby(['School_ID']).mean()[['Data_Handling']].sort_values(by="Data_Handling")
            p = df_selection.groupby('School_ID').mean()[["Data_Handling"]]
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
            fig.add_annotation(x=df["School_ID"], y=Final_Student_Analysis["Data_Handling"].mean(), showarrow=False, arrowhead=0 ,text='')
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