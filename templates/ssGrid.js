$(function() {
    const SERVICE_URL = "http://localhost:8000"

    var ssDataSource = new DevExpress.data.CustomStore({
        key: "OrderId",
        load: function(loadOptions) {
            var d = $.Deferred();
            var params = {};
 
            [
                "filter",
                "group", 
                "groupSummary",
                "parentIds",
                "requireGroupCount",
                "requireTotalCount",
                "searchExpr",
                "searchOperation",
                "searchValue",
                "select",
                "sort",
                "skip",     
                "take",
                "totalSummary", 
                "userData"
            ].forEach(function(i) {
                if(i in loadOptions && isNotEmpty(loadOptions[i])) {
                    params[i] = JSON.stringify(loadOptions[i]);
                }
            });
 
            $.getJSON( SERVICE_URL + "/{{ loadUrl }}", params )
                .done(function(response) {
                    d.resolve(response.data, { 
                        totalCount: response.totalCount,
                        summary: response.summary,
                        groupCount: response.groupCount
                    });
                })
                .fail(function() { throw "Data loading error" });
            return d.promise();
        },
    });
    

    $("#dataGridContainer").dxDataGrid({
        dataSource: ssDataSource,
        /*new DevExpress.data.CustomStore({
            loadMode: "raw", // omit in the DataGrid, TreeList, PivotGrid, and Scheduler
            load: function() {
                return $.getJSON(SERVICE_URL + "/{{loadUrl}}")
                    .fail(function() { throw "Data loading error" });
            },
        }),*/
        remoteOperations: true,
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
        export: {
            enabled: true,
            //allowExportSelectedData : true
        },
        onExporting: function(e) { 
            const workbook = new ExcelJS.Workbook(); 
            const worksheet = workbook.addWorksheet('Main sheet'); 
     
            DevExpress.excelExporter.exportDataGrid({ 
                worksheet: worksheet, 
                component: e.component 
            }).then(function() {
                workbook.xlsx.writeBuffer().then(function(buffer) { 
                    saveAs(new Blob([buffer], { type: 'application/octet-stream' }), 'DataGrid.xlsx'); 
                }); 
            });  
        }

    });
});

function isNotEmpty(value) {
    return value !== undefined && value !== null && value !== "";
}