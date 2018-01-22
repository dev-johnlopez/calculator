



function generateUnitForm(data) {
  var template = $('#unitForm').html();
  var info = Mustache.to_html(template,data);
  $('#units').append(info);
}

function addUnit() {
  var currentNumberOfUnits = $("#units > div").length;
  var data = {
    units: [
      {
        "id": currentNumberOfUnits,
        "unitNumber" : currentNumberOfUnits + 1,
        "formName": "unit",
        "fieldName": "rent",
        "value" : ""
      }
  ]};
  generateUnitForm(data);
}

function addUnitToForm() {
  addUnit()
}
