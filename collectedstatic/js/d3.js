$(function(){
    var loadImportResult = function(tablecontent, cls){
        // this approach is interesting if you need to dynamically create data in Javascript
        var metadata = [];
        metadata.push({ name: "username", label: "UserName", datatype: "string", editable: true});
        metadata.push({ name: "vmeare_id", label:"VMware Id", datatype: "string", editable: true});
        metadata.push({ name: "project", label: "Project Name", datatype: "string", editable: true});
        metadata.push({ name: "jobfunction", label: "Job Function", datatype: "string", editable: true});
        metadata.push({ name: "value", label: "Allocation Value", datatype: "integer", editable: true});
        var data = [];
        for (var i = 1; i < 1000; i++){
            data.push({id: i, values: {"vmeare_id": 121445, "value":33,"username":"Duke", project: "Core Service PRM", jobfunction: "Core Development"}});
        }

        editableGrid = new EditableGrid("DemoGridJsData");
        editableGrid.load({"metadata": metadata, "data": data});
        editableGrid.renderGrid(tablecontent, cls);
    }

    window.loadImportResult = loadImportResult;
});