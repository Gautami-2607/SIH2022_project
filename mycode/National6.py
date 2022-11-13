import pandas as pd  #DONE but correct o/p not coming for Pie chart
import plotly_express as px
import streamlit as st
"""st.set_page_config(page_title="National Dashboard",page_icon=":blue_book:",
                   layout="wide")"""
def national():
    df=pd.read_excel("D:\Student_Data_20.xlsx")
    #print(df)
    #st.dataframe(df)
    st.title(":blue_book: National Dashboard")
    st.markdown("###")

    def getschools(l):
        schools = []
        for j in l:
            for i in range(df.shape[0]):
                if (df.loc[i, "District_ID"] == j):
                    schools.append(df.loc[i, "School_ID"])
                    continue
                else:
                    pass
        return list(set(schools))

    def getdistricts(l):
        dist=[]
        for j in l:
            for i in range(len(df)):
                if(df.loc[i,"State_ID"]==j):
                    dist.append(df.loc[i,"District_ID"])
                    continue
                else:
                    pass
        return list(set(dist))

    st.sidebar.header("Select the Credentials here")

    year = st.sidebar.selectbox("Select the Year: ", options= df["Year"].unique())


    state=st.sidebar.multiselect("Select the state:",
                                 options=sorted(df["State_ID"].unique())
                                 )

    district_id = st.sidebar.multiselect(
        "Select the Districts:",#label
        #options = sort(df["District_ID"].unique()),
        options=getdistricts(state)
    )

    schools= st.sidebar.multiselect("Select the school:",options=getschools(district_id))

    gender = st.sidebar.multiselect(
        "Select the Gender:",# label
        options = ["Male", "Female", "Others"],
        default = ["Male", "Female","Others"]
    )


    #districts=st.sidebar.multiselect("Select the district:", options=getdistricts([state]))
    #schools=st.sidebar.multiselect("Select the school:",options=getschools(districts))
    df_selection=df.query(
        "State_ID==@state & Gender == @gender & Year ==@year"
    )

    df_selection2 = df.query(
        "State_ID==@state & District_ID==@district_id & Gender==@gender & Year ==@year"
        )

    df_selection3 = df.query(
        "State_ID==@state & District_ID==@district_id & School_ID==@schools & Gender==@gender & Year ==@year"
        )




    st.markdown("""<h3> National-Level Analysis </h3>""", unsafe_allow_html=True)
    md= df.groupby(['State_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
    md1 = md["Final_Result"].mean()
    e= st.sidebar.number_input("Select the criteria",min_value=5.0,max_value=df_selection["Final_Result"].max(),value= md["Final_Result"].mean())


    Final_State_Analysis = df.groupby(['State_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
    import plotly.graph_objects as go
    p = df.groupby('State_ID').mean()[["Final_Result"]]
    x = p.index
    y = p["Final_Result"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(font_family="Rockewell",
                      legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    color_discrete_sequence =['#000080']*3
    fig.update_traces(marker_color='#000080')
    fig.add_shape(type="line", line_color="red", line_width= 2, opacity=1, x0=0, x1= md1 , xref="paper",
                 y0=md1 , y1=md1 , yref="y")
    fig.add_annotation(x=df["State_ID"], y=Final_State_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='Target')
    #fig.show()
    st.plotly_chart(fig)
    st.markdown("---")


    ##################################
    st.sidebar.text("Select the visualization mode for \ndesired states:")

    b=st.sidebar.button("BARGRAPH")
    a = st.sidebar.button("PIECHART")

    st.markdown("""<h3>Analysis Among Desired States  </h3>""", unsafe_allow_html=True)
    if(b):
        Final_Student_Analysis = df_selection.groupby(['State_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
        import plotly.graph_objects as go
        p = df_selection.groupby('State_ID').mean()[["Final_Result"]]
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
        fig.add_annotation(x=df["State_ID"], y=Final_Student_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text=''
        )
        #fig.show()
        st.plotly_chart(fig)

    if(a):
        pc_data= df_selection.groupby(['State_ID']).mean()[['Final_Result']].sort_values(
            by="Final_Result")
        pc1 = px.pie(values=pc_data["Final_Result"],names=pc_data.index)
        st.plotly_chart(pc1)


    ##############################################
    st.markdown("---")


    st.markdown("""<h3>Analysis Among Desired Districts </h3>""", unsafe_allow_html=True)
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
    if(e>=5):
        fig.add_shape(type="line", line_color="red", line_width=2, opacity=1, x0=0, x1=e, xref="paper",
                  y0=e, y1=e, yref="y")
    fig.add_annotation(x=df["State_ID"], y=Final_District_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='')
        #fig.show()
    st.plotly_chart(fig)


    ###########################################
    st.markdown("---")


    st.markdown("""<h3>Analysis Among Schools Present In Districts </h3>""", unsafe_allow_html=True)
    Final_School_Analysis = df_selection2.groupby(['School_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")

    import plotly.graph_objects as go
    p = df_selection2.groupby('School_ID').mean()[["Final_Result"]]
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


    ################################
    st.markdown("---")
    st.markdown("""<h3>Analysis Among Desired Schools </h3>""", unsafe_allow_html=True)
    Final_School_Analysis = df_selection3.groupby(['School_ID']).mean()[['Final_Result']].sort_values(by="Final_Result")
    p = df_selection3.groupby('School_ID').mean()[["Final_Result"]]
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
    fig.add_annotation(x=df["School_ID"], y=Final_School_Analysis["Final_Result"].mean(), showarrow=False, arrowhead=1,text='')
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