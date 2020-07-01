function oneOnOne(oneOnOneBtn) {
    console.log(oneOnOneBtn)
  let relationType = oneOnOneBtn.parentNode.children[0];
  relationType.value = "oneOnOne";
  let oneOnOneDiv = oneOnOneBtn.parentNode.parentNode.children[5].children[1];
  let oneOnManyDiv = oneOnOneBtn.parentNode.parentNode.children[6].children[1];
  let manyOnManyDiv = oneOnOneBtn.parentNode.parentNode.children[7].children[1];

  oneOnOneDiv.style.display = "block";
  oneOnManyDiv.style.display = "none";
  manyOnManyDiv.style.display = "none";
  let oneOnManyBtn = oneOnOneBtn.parentNode.parentNode.children[4].children[1];
  let manyOnManyBtn = oneOnOneBtn.parentNode.parentNode.children[4].children[2];
  oneOnOneBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #c2bdbd 5%, #c7c5c5 100%); color: white;"
  );
  oneOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%); color:#666666;"
  );
  manyOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);color:#666666;"
  );
  return;
}
function oneOnMany(oneOnManyBtn) {
  let relationType = oneOnManyBtn.parentNode.children[0];
  relationType.value = "oneOnMany";
  let oneOnOneDiv = oneOnManyBtn.parentNode.parentNode.children[5].children[1];
  let oneOnManyDiv = oneOnManyBtn.parentNode.parentNode.children[6].children[1];
  let manyOnManyDiv =
    oneOnManyBtn.parentNode.parentNode.children[7].children[1];
  oneOnOneDiv.style.display = "none";
  oneOnManyDiv.style.display = "block";
  manyOnManyDiv.style.display = "none";
  let oneOnOneBtn = oneOnManyBtn.parentNode.parentNode.children[4].children[0];
  let manyOnManyBtn =
    oneOnManyBtn.parentNode.parentNode.children[4].children[2];
  oneOnOneBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%); color:#666666;"
  );
  oneOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #c2bdbd 5%, #c7c5c5 100%); color: white;"
  );
  manyOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);color:#666666;"
  );
  return;
}
function manyOnMany(manyOnManyBtn) {
  let relationType = manyOnManyBtn.parentNode.children[0];
  relationType.value = "manyOnMany";
  let oneOnOneDiv = manyOnManyBtn.parentNode.parentNode.children[5].children[1];
  let oneOnManyDiv =
    manyOnManyBtn.parentNode.parentNode.children[6].children[1];
  let manyOnManyDiv =
    manyOnManyBtn.parentNode.parentNode.children[7].children[1];

  oneOnOneDiv.style.display = "none";
  oneOnManyDiv.style.display = "none";
  manyOnManyDiv.style.display = "block";
  let oneOnOneBtn = manyOnManyBtn.parentNode.parentNode.children[4].children[0];
  let oneOnManyBtn =
    manyOnManyBtn.parentNode.parentNode.children[4].children[1];
  oneOnOneBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%); color:#666666;"
  );
  oneOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);color:#666666;"
  );
  manyOnManyBtn.setAttribute(
    "style",
    "background:linear-gradient(to bottom, #c2bdbd 5%, #c7c5c5 100%); color: white;"
  );
  return;
}

function filterPrimaryKeys(keysPerTable, tableSelect) {
  keysSelect = tableSelect.parentNode.children[2];
  console.log(keysSelect)
  if (document.getElementById("oneOnOneKeys1").childElementCount > 0) {
    keysSelect.innerHTML = "";
  }
  let selectedFilter = tableSelect.value;

  let keys = [];
  let values = [];
  for (let i = 0; i < keysPerTable.length; i++) {
    keys[i] = Object.keys(keysPerTable[i]);
    values[i] = Object.values(keysPerTable[i]);
  }
  for (let i = 0; i < keysPerTable.length; i++) {
    if (keys[i][0] == selectedFilter) {
      let option = document.createElement("option");
      option.text = values[i][0];
      option.text = option.text.split("-")[0];
      option.value = option.text.split("-")[0];
      keysSelect.appendChild(option);
    }
  }
}
function filterPrimaryKeys2(keysPerTable) {
  keysSelect = document.getElementById("oneOnOneKeys2");
  if (document.getElementById("oneOnOneKeys2").childElementCount > 0) {
    keysSelect.innerHTML = "";
  }
  let selectedFilter = document.getElementById("oneOnOneTable2").value;
  let keys = [];
  let values = [];
  for (let i = 0; i < keysPerTable.length; i++) {
    keys[i] = Object.keys(keysPerTable[i]);
    values[i] = Object.values(keysPerTable[i]);
  }
  for (let i = 0; i < keysPerTable.length; i++) {
    if (keys[i][0] == selectedFilter) {
      let option = document.createElement("option");
      option.value = keysPerTable[i][0];
      option.text = values[i][0];
      keysSelect.appendChild(option);
    }
  }
}
