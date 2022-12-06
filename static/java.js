// REFERENCE https://www.w3schools.com/js/js_validation.asp

function validateTellAdvice() {

  let text = document.forms["tell"]["tell_advice"].value;
  let tag = document.forms["tell"]["tell_tags"].value;

  if (text == "") {
    window.alert("Please share some advice!");
    return false;
  }

  if (tag == "") {
    window.alert("Please tag your advice!");
    return false;
  }

}



function validateTellStory() {

  let text2 = document.forms["tell2"]["tell_story"].value;
  let tag2 = document.forms["tell2"]["tell_tags"].value;

  if (text2 == "") {
    window.alert("Please tell your story!");
    return false;
  }

  if (tag2 == "") {
    window.alert("Please tag your story!");
    return false;
  }

}
