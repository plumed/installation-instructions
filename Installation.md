# Installation

The instructions that follow explain how to configure, compile and install a single version of plumed on a local machine.  For most users the instructions 
below will work fine.  A small fraction of users will want to do something more complicated at install time.  Such users can 
use the "How would you like to build PLUMED" button below to get instructions on what to do in these more exotic cases.  

It is perhaps easiest to install PLUMED using the macports or conda package manager.  For instructions on how to install PLUMED in this way "How would you like to build PLUMED" button. 

You will find a "show defaults" button by the boxes that shows a configure command below.  If you click this button the default flags that are used when that command is executed are shown.
Information on what is controlled by each flag is provided through tooltips, which you are shown if you hover over the flag.  

Some flags are shown in bold in the short versions of the configure commands below.  Clicking on these commands will open a pop-up window that contains further information 
about the flag.  You will most likely not need to worry about the information in these pop ups but it may be worth considering as these options can affect the performance of the
compiled code.

PLUMED can be used in tandem with the MD codes shown in the table on the right below.  To see instructions on what you must do in order have versions
of these codes that work with PLUMED click the checkbox associated with the code you require.  Instructions on patching the code you select with PLUMED 
will appear at the bottom of the web page.

{% raw %}
<style>
  pre {
    overflow-x: auto;
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
  }
</style>
<script>
function showData( name, indiv ) {
 var mydiv = document.getElementById(indiv);
 var mydata = document.getElementById(name);
 mydiv.innerHTML = mydata.innerHTML;
 showInstructions(current_instructions);
}
function showMinimalConfigure(name) {
  var btn = document.getElementById(name + "_button");
  var mydiv = document.getElementById("conf_" + name);
  btn.textContent = "show defaults"; 
  var dataField = document.getElementById(name + "_short");
  mydiv.innerHTML = dataField.innerHTML;
}

function swapConfigure(name) {
 if( btn.textContent=="show defaults" ) { 
   var btn = document.getElementById(name + "_button");
   var mydiv = document.getElementById("conf_" + name);
   btn.textContent = "hide defaults";
   var dataField = document.getElementById(name + "_long");
   mydiv.innerHTML = dataField.innerHTML;
 } else if( btn.textContent=="hide defaults" ) {
   showMinimalConfigure(name);
 }
}
function openModal( name ) {
 var mymodal = document.getElementById( name );
 mymodal.style.display = "block";  
}
window.onload = function(event) {
 showInstructions("local");
}
</script>

{% endraw %}
