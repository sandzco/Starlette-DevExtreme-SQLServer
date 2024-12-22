$(function() {
    const SERVICE_URL = "http://localhost:8000"

    $("#dataGridContainer").dxDataGrid({
        dataSource: new DevExpress.data.CustomStore({
            loadMode: "raw", // omit in the DataGrid, TreeList, PivotGrid, and Scheduler
            load: function() {
                return $.getJSON(SERVICE_URL + "/{{loadUrl}}")
                    .fail(function() { throw "Data loading error" });
            },
        }),
        rowAlternationEnabled: true,
        hoverStateEnabled: true,
        allowColumnResizing: true,
        columnAutoWidth: true,
        contextMenuEnabled: true,
        filterRow: { visible: true },
        paging: {
            pageSize : 25
        },
        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [25, 50, 75, 100],
            showNavigationButtons: true,
        },
    });
});