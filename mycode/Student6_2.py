import pandas as pd
import plotly_express as px
import streamlit as st
import plotly.graph_objects as go
st.set_page_config(page_title="Student Dashboard",page_icon=":blue_book:",
                   layout="wide")
df=pd.read_excel("Student_data_4.xlsx")
#print(df)
#st.dataframe(df)
st.title(":blue_book: Student Dashboard")
st.markdown("##")# inserting paragraph here to seperate title from KPI's

def getdistricts(l):
    dist=[]
    for i in range(len(df)):
        if(df.loc[i,"State_ID"]==l):
            dist.append(df.loc[i,"District_ID"])
            continue
        else:
            pass
    return list(set(dist))


def getstudents(l):
    students = []
    for i in range(df.shape[0]):
        if (df.loc[i, "School_ID"] == l):
            students.append(df.loc[i, "Student_ID"])
        else:
            pass
    return students


st.sidebar.header("Select the Credentials here")
schools=st.sidebar.selectbox("Select the school:",options=df["School_ID"].unique())
students=st.sidebar.selectbox("Select the students:",options= getstudents(schools)) #
year = st.sidebar.selectbox("Select the Year: ", options= df["Year"].unique())


df_selection=df.query(
    "School_ID==@schools & Student_ID==@students & Year ==@year"
)

cls=[ 'Oral', 'Decoding', 'Reading', 'Writing', 'Speaking ',
       'Concept_Understanding', 'Statistics', 'Spatial_Understanding',
       'Measurement', 'Data_Handling' ]
#r_data= df_selection[['Oral','Decoding ']].sort_values(
       # by=["Oral","Decoding "])
#pd1 = px.pie(df_selection,names=[ 'Oral', 'Decoding ', 'Reading', 'Writing', 'Speaking ',
  #     'Concept_Understanding ', 'Statistics ', 'Spatial_Understanding ',
 #      'Measurement ', 'Data_Handling ' ], color_discrete_sequence=["#0083B8"])
sd= df.query(" Student_ID==@students ")
pd1 = px.bar(sd,
    y= "Student_ID" ,# "Decoding"  # value on x axis
    x=[ 'Oral', 'Decoding', 'Reading', 'Writing', 'Speaking',
       'Concept_Understanding', 'Statistics', 'Spatial_Understanding',
       'Measurement', 'Data_Handling', 'Final_Result' ],
    orientation="v",  # horizaontal barchart
    title="<b> STUDENT V/S SKILLS </b>",  # html formattng elements
    color_continuous_scale=cls,
    #pattern_shape_sequence=cls,
    template="plotly_white",  # inbuilt in plotly
    # color=Final_Student_Analysis.index
)
e = st.sidebar.number_input("Select the criteria", min_value=5.0, max_value=10.0,
                            value=5.0)
skills=st.sidebar.selectbox("select any skill:",options=['Oral','Decoding', 'Reading', 'Writing', 'Speaking',
       'Concept_Understanding', 'Statistics', 'Spatial_Understanding',
       'Measurement', 'Data_Handling', 'Final_Result'])
st.sidebar.text("choose the visualization technique")

b=st.sidebar.button("BARGRAPH")
a=st.sidebar.button("PIECHART")

if(a):
    #if(clms=="Student"):
    if(skills=="Oral"):
        pc_data= df_selection.groupby(['Student_ID']).sum()[['Oral']].sort_values(
        by="Oral")
        pc1 = px.pie(values=pc_data["Oral"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Decoding"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Decoding']].sort_values(
            by="Decoding")
        pc1 = px.pie(values=pc_data["Decoding"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Reading"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Reading']].sort_values(
            by="Reading")
        pc1 = px.pie(values=pc_data["Reading"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Writing"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Writing']].sort_values(
            by="Writing")
        pc1 = px.pie(values=pc_data["Writing"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Speaking"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Speaking']].sort_values(
            by="Speaking")
        pc1 = px.pie(values=pc_data["Speaking"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Spatial_Understanding"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Spatial_Understanding']].sort_values(
            by="Spatial_Understanding")
        pc1 = px.pie(values=pc_data["Spatial_Understanding"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Measurement"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Measurement']].sort_values(
            by="Measurement")
        pc1 = px.pie(values=pc_data["Measurement"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Data_Handling"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Data_Handling']].sort_values(
            by="Data_Handling")
        pc1 = px.pie(values=pc_data["Data_Handling"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Concept_Understanding"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Concept_Understanding']].sort_values(
            by="Concept_Understanding")
        pc1 = px.pie(values=pc_data["Concept_Understanding"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Statistics"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Statistics']].sort_values(
            by="Statistics")
        pc1 = px.pie(values=pc_data["Statistics"],names=pc_data.index)
        st.plotly_chart(pc1)
    if (skills=="Final_Result"):
        pc_data = df_selection.groupby(['Student_ID']).sum()[['Final_Result']].sort_values(
            by="Final_Result")
        pc1 = px.pie(values=pc_data["Final_Result"],names=pc_data.index)
        st.plotly_chart(pc1)    
if(b):

    if(skills=="Oral"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Oral']].sort_values(by="Oral")
        p = df_selection.groupby('Student_ID').mean()[["Oral"]]
        x = p.index
        y = p["Oral"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if(e>=5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                      xref="paper",
                      y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Oral"].mean(),
                           arrowhead=1, showarrow=False)
        # fig.show()
        st.plotly_chart(fig)
        st.plotly_chart(fig)
    if (skills=="Decoding"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Decoding']].sort_values(by="Decoding")
        p = df_selection.groupby('Student_ID').mean()[["Oral"]]
        x = p.index
        y = p["Decoding"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if(e>=5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                      xref="paper",
                      y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Decoding"].mean(),
                           arrowhead=1, showarrow=False)
        # fig.show()
        st.plotly_chart(fig)
    if (skills=="Reading"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Reading']].sort_values(by="Reading")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Reading"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Reading"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Writing"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Writing']].sort_values(by="Writing")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Writing"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if(e>=5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                      xref="paper",
                      y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Writing"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Speaking"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Speaking']].sort_values(by="Speaking")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Speaking"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Speaking"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Concept_Understanding"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Concept_Understanding']].sort_values(by="Concept_Understanding")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Concept_Understanding"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Concept_Understanding"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Spatial_Understanding"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Spatial_Understanding']].sort_values(by="Spatial_Understanding")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Spatial_Understanding"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Spatial_Understanding"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Statistics"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Statistics']].sort_values(by="Statistics")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Statistics"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Statistics"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Measurement"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Measurement']].sort_values(by="Measurement")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Measurement"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Measurement"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
    if (skills=="Data_Handling"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Data_Handling']].sort_values(by="Data_Handling")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Data_Handling"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Data_Handling"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)

    if (skills=="Final_Result"):
        Final_Student_Analysis = df_selection.groupby(['Student_ID']).sum()[['Final_Result']].sort_values(by="Final_Result")
        x = Final_Student_Analysis.index
        y = Final_Student_Analysis["Final_Result"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y))
        fig.update_layout(font_family="Rockewell",
                          legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
        if (e >= 5):
            fig.add_shape(type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot", x0=0, x1=e,
                          xref="paper",
                          y0=e, y1=e, yref="y")
        fig.add_annotation(text="Target", x=df["Student_ID"], y=Final_Student_Analysis["Final_Result"].mean(),
                           arrowhead=1, showarrow=False)
        st.plotly_chart(fig)
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
 footer {visibility: hidden;}
 header {visibility: hidden;}
 </style>
 """               
st.markdown(hide_st_style, unsafe_allow_html= True)
