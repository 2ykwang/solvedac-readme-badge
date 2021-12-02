const elementsArray = document.querySelectorAll(
  ".form-control,.form-check-input,.form-select"
);

const elementMapping = {
  user: "string",
  theme: "string",
  size: "string",
  back_color: "color",
  common_color: "color",
  sub_color: "color",
  border_color: "color",
  compact: "boolean",
  use_back_color: "boolean",
  use_border: "boolean",
  use_shadow: "boolean",
};
const previewImg = document.getElementById("preview-img");
const markdownBlock = document.getElementById("markdown");
const userElement = document.getElementById("user");
const linkElement = document.getElementById("link");

const host = location.protocol.concat("//").concat(window.location.host);

const handleChange = (e) => {
  const searchParams = new URLSearchParams(window.location.search);
  const target = e.target;
  for (key in elementMapping) {
    const element = document.getElementById(key);
    if (element !== undefined) {
      if (elementMapping[key] === "string") {
        searchParams.append(key, element.value);
      } else if (elementMapping[key] === "color") {
        const use_color = document.getElementById(`use_custom_${key}`);
        if (use_color && use_color.checked) {
          searchParams.append(key, element.value.replace("#", ""));
        }
      } else {
        searchParams.append(key, element.checked ? "1" : "0");
      }
    }
  }
  const imgUrl = `${host}/api/v1/badge?${searchParams.toString()}`;
  let markdownText = `![${user.value}](${imgUrl})`;
  
  if(linkElement.value){
      markdownText = `[${markdownText}](${linkElement.value})`
  }  

  markdownBlock.innerText = markdownText;
  hljs.highlightElement(markdownBlock);
  previewImg.src = imgUrl;
};

// 입력 폼 안에 있는 요소들 이벤트 추가
elementsArray.forEach((elem) => {
  elem.addEventListener("change", handleChange);
});

const copyCode = (e)=>{ 
  navigator.clipboard.writeText(markdownBlock.innerText);
}