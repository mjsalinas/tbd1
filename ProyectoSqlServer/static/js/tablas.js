function addTableField() {
  let lastField = document.getElementById("new-fields-area").lastElementChild;
  let newLastField = lastField.cloneNode(true);
  let area = document.getElementById("new-fields-area");
  area.appendChild(newLastField);
  return;
}

function removeTableField() {
  let newFieldsCount = document.getElementById("new-fields-area")
    .childElementCount;
  if (newFieldsCount<= 2) {
    return;
  }
  let fieldToRemove = document.getElementById("new-fields-area");
  fieldToRemove = fieldToRemove.children[1];
  console.log(fieldToRemove)

  fieldToRemove = fieldToRemove.children;
  console.log(fieldToRemove)

  let newField = fieldToRemove.parentNode;
  newField.parentNode.removeChild(newField);
}

function handleOnClickPK(input) {
  let hiddenFlag = document.getElementById("hidden-flag").children[0];
  let isNull = input.parentNode.parentNode.parentNode.children;
  if (isNull.length == 2){
    isNull = input.parentNode.parentNode.parentNode.children[1].children[0].children[0];
  }else if(isNull.length == 3){
    isNull = input.parentNode.parentNode.parentNode.children[2].children[0].children[0];
  }
  hiddenFlag = hiddenFlag.children[0];
  if (input.checked) {
    hiddenFlag.value = "true";
    isNull.value = "false";
  } else if (!input.checked) {
    hiddenFlag.value = "false";
  }
  return input;
}

function handleOnClickFk(input) {
  let hiddenFlag = input.parentNode;
  hiddenFlag = hiddenFlag.children[0]
  // parentNode.parentNode.parentNode. children[0].children[1].children[1];
  let relationsDiv = input.parentNode.parentNode.parentNode.parentNode.children[0].children[1].children[1];
  if (input.checked) {
    hiddenFlag.value = "true";
    relationsDiv.style.display = "block";
    return;
  }
  hiddenFlag.value = "false";
  relationsDiv.style.display = "none";
  return;
}
function handleIsNullable(input) {
  let hiddenFlag = input.parentNode.parentNode;
  hiddenFlag = hiddenFlag.children[0].children[0];
  if (input.checked) {
    hiddenFlag.value = "true";
  } else if (!input.checked) {
    hiddenFlag.value = "false";
  }
  return input;
}
