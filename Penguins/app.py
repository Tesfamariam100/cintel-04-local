import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from shiny import reactive, render
import seaborn as sns
import pandas as pd
from palmerpenguins import load_penguins
import palmerpenguins

# Load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Add a reactive calculation to filter the data
@reactive.calc
def filtered_data():
    selected_species = input.selected_species_list()
    return penguins_df[penguins_df['species'].isin(selected_species)]


# Set the page title
ui.page_opts(title="Penguins Data Tesfamariam", fillable=True)

# Create a Shiny UI sidebar
with ui.sidebar(open="open"):
    ui.h4("Sidebar")
    ui.input_selectize("selected_attribute",
            "Select Attribute",
            ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
            )
    # The `selectize` function in the Shiny UI sidebar is creating an input element that
    # allows users to select multiple options with a search and select interface. It provides
    # a dropdown with search functionality and the ability to select multiple values, making
    # it easier for users to filter and interact with the data based on the available
    # options.
    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 10)
    ui.input_slider("seaborn_bin_count", "Seaborn Bin Count", 1, 100, 50)
    ui.input_checkbox_group("selected_species_list", "Select Species", 
    ["Adelie", "Gentoo", "Chinstrap"],
    selected=["Adelie"], inline=False)
    ui.hr()
    ui.a("My GitHub Repo", href="https://github.com/Tesfamariam100/cintel-03-reactive", target="_blank")

# Display a DataTable and a Data Grid
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.h4("Penguin Data Table")
        with ui.div(style="height: 400px; overflow-y: auto;"):
            @render.data_frame
            def penguins_datatable():
                return render.DataTable(filtered_data()) 

    with ui.card(full_screen=True):
        ui.h4("Penguin Data Grid")
        with ui.div(style="height: 400px; overflow-y: auto;"):
            @render.data_frame
            def penguins_grid():
                return render.DataGrid(filtered_data())

# added a horizontal rule
ui.hr()

# Create a layout for the graphs
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Histogram")
        @render_plotly
        def plotly_histogram():
            return px.histogram(filtered_data(), 
                                x=input.selected_attribute(),
                                nbins=input.plotly_bin_count(),
                                color="species").update_layout(height=600)

    with ui.card(full_screen=True):
        ui.card_header("Plotly Scatterplot")
        @render_plotly
        def plotly_scatterplot():
            return px.scatter(filtered_data(),
                            x=input.selected_attribute(),
                            y="flipper_length_mm",
                            color="species", 
                            title="Plotly Scatterplot: Species").update_layout(height=600)

    with ui.card(full_screen=True):
        ui.card_header("Seaborn Histogram")
        @render.plot
        def seaborn_histogram():
            return sns.histplot(filtered_data(),
                                x=input.selected_attribute(),
                                bins=input.plotly_bin_count(),
                                kde=True)
