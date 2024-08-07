from fasthtml.common import * 

styles_and_scripts = (
    Script(src="https://cdn.jsdelivr.net/npm/ag-grid-community/dist/ag-grid-community.min.js"),
    Style(rel="stylesheet", src="https://cdn.jsdelivr.net/npm/ag-grid-community@32.0.0/styles/ag-grid.css"),
    Style(rel="stylesheet", src="https://cdn.jsdelivr.net/npm/ag-grid-community@32.0.0/styles/ag-theme-quartz.css")
)

app, rt = fast_app(hdrs=styles_and_scripts, default_hdrs=False, pico=False)


sample_ag_grid = """
    let gridApi;

    const gridOptions = {
        rowData: [
            { make: "Tesla", model: "Model Y", price: 64950 },
            { make: "Ford", model: "F-Series", price: 33850 },
            { make: "Toyota", model: "Corolla", price: 29600 },
            { make: "Mercedes", model: "EQA", price: 48890 },
            { make: "Fiat", model: "500", price: 15774 },
            { make: "Nissan", model: "Juke", price: 20675 },
        ],
        columnDefs: [
            { field: "make" },
            { field: "model" },
            { field: "price" },
            { field: "electric", checkboxSelection: true },
        ],
        defaultColDef: {
            flex: 1,
            },
        rowSelection: "multiple",
        rowMultiSelectWithClick: true,
    };
    gridApi = agGrid.createGrid(document.querySelector("#myGrid"), gridOptions);
"""

@rt("/ag-grid-demo")
def get():
    """FastHTML allows for css classes and styles to be inline. Mix and match as you will."""
    return (
        Title("Ag-Grid Demo with FastHTML"),
            Main(
                Div(
                    H1("Ag-Grid Demo with FastHTML",  style="font-family: 'Roboto', 'Helvetica', 'Arial', sans-serif; text-align: center; font-weight: 700;"),
                    Div(cls="ag-theme-quartz", id="myGrid", style="height: 600px; width: 100%;"),
                ),
                Script(sample_ag_grid)
            )
        )

serve()
