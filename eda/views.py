from collections import Counter
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
import pandas as pd

# Related to Plotly

from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px


#dict ={}
def eda(request):

    context = {}
    global attribute

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #check if this file ends with csv
        if uploaded_file.name.endswith('.csv'):
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file) #gets the name of the file

            d = os.getcwd() # how we get the current dorectory
            file_directory = d+'/media/'+name #saving the file in the media directory

            data = readfile(file_directory)

            print("Features:", data.columns.tolist())
            attribute = 'LoanAmountTerm'
            request.session['attribute'] = attribute

            if attribute not in data.axes[1]:
                messages.warning(request, 'Please write the column name correctly')
            else:
                return redirect(tables)

        else:
            messages.warning(request, 'File was not uploaded. Please use .csv file extension!')


    return  render(request, 'eda.html', context)


            #project_data.csv
def readfile(filename):

    #we have to create those in order to be able to access it around
    # use panda to read the file because i can use DATAFRAME to read the file
    #column;culumn2;column
    global rows,columns,data,my_file,missing_values
     #read the missing data - checking if there is a null
    missingvalue = ['?', '0', '--']

    my_file = pd.read_csv(filename, sep='[:;,|_]',na_values=missingvalue, engine='python')

    data = pd.DataFrame(data=my_file, index=None)
    print(data)

    rows = len(data.axes[0])
    columns = len(data.axes[1])


    null_data = data[data.isnull().any(axis=1)] # find where is the missing data #na null =['x1','x13']
    missing_values = len(null_data)



    return data



def results(request):

    plot_fig_LoanAmount, plot_fig_LS, plot_cor_fig, plot_fig_loan_dist, fig_loanbox, plot_fig_heat, plot_fig_Age= demo_plot_view()

    context = {

        'plot_fig_LoanAmount': plot_fig_LoanAmount,
        'plot_fig_LS': plot_fig_LS,
        'plot_cor_fig': plot_cor_fig,
        'plot_fig_loan_dist': plot_fig_loan_dist,
        "fig_loanbox": fig_loanbox,
        "plot_fig_heat": plot_fig_heat,
        "plot_fig_Age":plot_fig_Age,
    }

    return render(request, 'results.html', context)


def tables(request):

    # plot_fig_LoanAmount, plot_fig_LS, plot_cor_fig, plot_fig_loan_dist, fig_loanbox, plot_fig_heat = demo_plot_view()
    #
    # context = {
    #
    #     'plot_fig_LoanAmount': plot_fig_LoanAmount,
    #     'plot_fig_LS': plot_fig_LS,
    #     'plot_cor_fig': plot_cor_fig,
    #     'plot_fig_loan_dist': plot_fig_loan_dist,
    #     "fig_loanbox": fig_loanbox,
    #     "plot_fig_heat": plot_fig_heat
    # }
    df_head, df_describe, df_js=demo_table_view()







    context = {
        "df_head":df_head,
        "df_describe": df_describe,
        "df_js":df_js,
    }


    return render(request, 'tables.html', context)










def demo_table_view():
    df_head=data.head().to_html()
    df_describe=data.describe().to_html()
    df_headjs=data.head().to_json()

    col_json=data.columns.values.tolist()
    df_js={
    "col_name":col_json,
    "tbl_son": df_headjs

    }
    return df_head, df_describe, df_js











def demo_plot_view():
    """
    View demonstrating how to display a graph object
    on a web page with Plotly.
    """
    # PLT 1
    fig_LoanAmount = px.histogram(data, x = 'LoanAmount')
    plot_fig_LoanAmount = fig_LoanAmount.to_html()


    fig_Age = px.histogram(data, x = 'Age')
    plot_fig_Age = fig_Age.to_html()














    fig_loanbox = px.box(data, x="Gender", y="LoanAmount", color="PropertyArea",title="Box chart")
    fig_loanbox = fig_loanbox.to_html()


    # pLOT 2
    fig_LS = px.bar(data, x="PropertyArea", y="Gender", color="LoanStatus", title="Bar chart")


    plot_fig_LS=fig_LS.to_html()


    # Plot 3
    data2=data.dropna()
    data2=data2.rename(columns={"ApplicantIncome": "Income", "CoapplicantIncome": "CoIncome","LoanAmount": "Amount", "LoanAmountTerm": "Term"})

    cor_fig = px.scatter_matrix(data2,
        dimensions=["Income", "CoIncome", "Amount", "Term"],
        color="Gender")
    plot_cor_fig=cor_fig.to_html()


    # Plot 4

    fig_loan_dist = px.pie(data, values='LoanAmount', names='Gender', color='Gender')



    plot_fig_loan_dist=fig_loan_dist.to_html()

    z=data.corr()
    fig_heat = px.imshow(z, text_auto=True, aspect="auto")

    plot_fig_heat=fig_heat.to_html()





    return plot_fig_LoanAmount, plot_fig_LS, plot_cor_fig, plot_fig_loan_dist, fig_loanbox, plot_fig_heat, plot_fig_Age
