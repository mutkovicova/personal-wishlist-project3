document.addEventListener("DOMContentLoaded", function () {
    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // tabs initialization
    let tabs = document.querySelectorAll('.tabs');
    M.Tabs.init(tabs);
});