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
            { make: "BMW", model: "3 Series", price: 41250 },
            { make: "Audi", model: "A4", price: 39900 },
            { make: "Chevrolet", model: "Malibu", price: 24495 },
            { make: "Honda", model: "Civic", price: 22750 },
            { make: "Hyundai", model: "Elantra", price: 20050 },
            { make: "Kia", model: "Soul", price: 18790 },
            { make: "Mazda", model: "CX-5", price: 25800 },
            { make: "Subaru", model: "Outback", price: 26995 },
            { make: "Volkswagen", model: "Golf", price: 23500 },
            { make: "Volvo", model: "XC60", price: 45650 },
            { make: "Jeep", model: "Wrangler", price: 28995 },
            { make: "Lexus", model: "RX 350", price: 45725 },
            { make: "Porsche", model: "Cayenne", price: 69000 },
            { make: "Jaguar", model: "XF", price: 51200 },
            { make: "Land Rover", model: "Range Rover", price: 92150 },
            { make: "Mitsubishi", model: "Outlander", price: 25795 },
            { make: "Infiniti", model: "Q50", price: 42100 },
            { make: "Acura", model: "TLX", price: 38650 },
            { make: "Genesis", model: "G70", price: 37650 },
            { make: "Cadillac", model: "CT5", price: 37495 },
            { make: "Buick", model: "Enclave", price: 42695 },
            { make: "Chrysler", model: "300", price: 30395 },
            { make: "Dodge", model: "Charger", price: 31950 },
            { make: "GMC", model: "Acadia", price: 36200 },
            { make: "Lincoln", model: "Nautilus", price: 43495 },
            { make: "Mini", model: "Cooper", price: 22900 },
            { make: "Alfa Romeo", model: "Giulia", price: 43100 },
            { make: "Bentley", model: "Bentayga", price: 177000 },
            { make: "Ferrari", model: "Roma", price: 218670 },
            { make: "Maserati", model: "Ghibli", price: 77200 }
        ],
        columnDefs: [
            { field: "make", filter: true },
            { field: "model" },
            { field: "price", valueFormatter: p => '$' + p.value.toLocaleString() },
            { field: "electric", checkboxSelection: true },
        ],
        defaultColDef: {
            flex: 1,
            },
        rowSelection: "multiple",
        rowMultiSelectWithClick: true,
        pagination: true,
        paginationPageSize: 10,
        paginationPageSizeSelector: [10, 25, 50],
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
