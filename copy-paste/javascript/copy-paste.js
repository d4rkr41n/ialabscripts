// ==UserScript==
// @name         vmware copy and paste
// @namespace    ?
// @version      0.2
// @description  from Mike Cutshaw, who got part of it from Alex Gartner
// @match        https://vcloud.ialab.dsu.edu/cloud/WebMKSConsole.html
// ==/UserScript==

$("body").bind("paste", function(e) {
    var data = e.originalEvent.clipboardData.getData('Text');
    data = data.replace(/\r/g, '');
    $("#console").wmks("sendInputString", data);
    document.getElementById("mainCanvas").focus();
});