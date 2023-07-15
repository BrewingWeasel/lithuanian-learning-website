const linkedVals = {
  "the_word": ["text", "morphed_word", "$"],
  "the_word_lemma": ["text", "lemma", "($)"],
  "verb_vals": ["text", "verb_values", "$"],
  "gender": ["text", "gender", "$"],
  "wiktionary_link": [
    "href",
    "lemma",
    "https://en.wiktionary.org/wiki/$#Lithuanian",
  ],
  "forvo_link": ["href", "lemma", "https://forvo.com/search/$/lt/"],
  "dict_link": ["href", "lemma", "http://www.lietuviu-anglu.com/$"],
};

const cases = {
  "Ins": "Instrumental",
  "Gen": "Genitive",
  "Acc": "Accusative",
  "Nom": "Nominative",
  "Loc": "Locative",
  "Dat": "Dative",
  "Voc": "Vocative",
};

const numbers = {
  "Plur": "Plural",
  "Sing": "Singular",
};

const words = document.getElementsByClassName("word");

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function formatWords(string, formatting) {
  if (string == null) {
    return "";
  }
  return capitalize(formatting.replace("$", string));
}

const setDetails = function () {
  for (const property in linkedVals) {
    const [replaceType, source, formatting] = linkedVals[property];
    if (replaceType === "text") {
      document.getElementById(property).textContent = formatWords(
        this.getAttribute(source),
        formatting,
      );
    } else {
      document.getElementById(property).href = formatWords(
        this.getAttribute(source),
        formatting,
      );
    }
  }
  if (this.getAttribute("case")) {
    const wordCase = this.getAttribute("case");
    document.getElementById("case_morphology").innerHTML =
      `<a id="case" class="${wordCase}" href="${cases[wordCase]}">${
        cases[wordCase]
      }</a> ${numbers[this.getAttribute("number")]} form of ${
        this.getAttribute("lemma")
      }`;
  } else {
    document.getElementById("case_morphology").textContent = "";
  }
};

Array.from(words).forEach(function (element) {
  element.addEventListener("click", setDetails);
});
