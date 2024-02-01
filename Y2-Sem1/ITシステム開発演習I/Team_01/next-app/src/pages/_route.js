import Router from "next/router";
const movePage = (url) => () => {
  Router.push(url);
};
export default movePage;
