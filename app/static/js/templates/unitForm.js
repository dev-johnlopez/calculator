



function generateUnitForm(data) {
  var template = $('#unitForm').html();
  var info = Mustache.to_html(template,data);
  $('#units').append(info);
}

function addUnit() {
  var currentNumberOfUnits = $("#units > div").length;
  alert(currentNumberOfUnits);
  var data = {
    units: [
      {
        "id": currentNumberOfUnits,
        "unitNumber" : currentNumberOfUnits + 1,
        "formName": "units",
        "fieldName": "income",
        "value" : ""
      }
  ]};
  generateUnitForm(data);
}

function addUnitToForm() {
  addUnit();
}
