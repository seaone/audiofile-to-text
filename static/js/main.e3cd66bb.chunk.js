(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{89:function(e,t,a){},97:function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),r=a(32),s=a.n(r),i=(a(89),a(39)),o=a.n(i),l=a(49),j=a(13),d=a(157),u=a(158),b=a(159),p=a(154),x=a(160),O=a(161),h=a(151),m=a(148),f=a(152),v=a(165),g=a(164),w=a(153),y=a(149),N=function(){var e=Object(l.a)(o.a.mark((function e(t){var a,n,c;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=t.file,n=t.lang,(c=new FormData).append("file",a),c.append("lang",n),e.abrupt("return",fetch("".concat("","/process"),{method:"post",body:c}).then((function(e){return e.json()})).catch((function(e){return e})));case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),S=a(2),k=Object(y.a)({container:{paddingTop:"4rem"},formBox:{display:"flex",alignItems:"flex-end",gap:"1rem",marginBottom:"2rem"},paper:{padding:"2rem"},button:{height:"40px"},inputWrapper:{flexGrow:1},box:{marginBottom:"2rem"},loader:{position:"absolute",top:"50%",left:"50%",marginTop:"-12px",marginLeft:"-12px"},audio:{width:"100%"}});var B=function(){var e=Object(n.useState)(""),t=Object(j.a)(e,2),a=t[0],c=t[1],r=Object(n.useState)(""),s=Object(j.a)(r,2),i=s[0],y=s[1],B=Object(n.useState)(""),C=Object(j.a)(B,2),T=C[0],W=C[1],z=Object(n.useState)(!1),D=Object(j.a)(z,2),E=D[0],I=D[1],A=Object(n.useState)(null),F=Object(j.a)(A,2),J=F[0],L=F[1],P=Object(n.useState)(!1),G=Object(j.a)(P,2),H=G[0],K=G[1],M=Object(n.useState)(""),R=Object(j.a)(M,2),U=R[0],_=R[1],q=Object(n.useState)(""),Q=Object(j.a)(q,2),V=Q[0],X=Q[1],Y=Object(n.useState)(!1),Z=Object(j.a)(Y,2),$=Z[0],ee=Z[1],te=function(){var e=Object(l.a)(o.a.mark((function e(){var t;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(I(!0),se(),null==J){e.next=18;break}return e.prev=3,e.next=6,N({file:J,lang:U});case 6:t=e.sent,W("".concat("","/").concat(t.file_path,"?updated=").concat(Date.now())),c(t.text),y(t.keywords.map((function(e){return e[0]})).join(", ")),e.next=18;break;case 12:e.prev=12,e.t0=e.catch(3),X("Something went worng :("),ee(!0),se(),console.error(e.t0);case 18:I(!1);case 19:case"end":return e.stop()}}),e,null,[[3,12]])})));return function(){return e.apply(this,arguments)}}(),ae=!E,ne=!E,ce=!E&&H,re=!E&&H&&""!==U,se=function(){W(""),c(""),y("")},ie=k();return Object(S.jsx)("div",{className:"App",children:Object(S.jsxs)(d.a,{className:ie.container,maxWidth:"md",children:[Object(S.jsx)(u.a,{variant:"h1",component:"h1",gutterBottom:!0,children:"Audiofile to text"}),Object(S.jsxs)(b.a,{className:ie.formBox,children:[Object(S.jsxs)(p.a,{children:[Object(S.jsx)(x.a,{children:"Select file"}),Object(S.jsxs)(O.a,{component:"label",variant:"outlined",disabled:!ae,className:ie.button,children:["Upload File (.wav)",Object(S.jsx)("input",{type:"file",accept:"audio/wav",hidden:!0,onChange:function(e){var t=e.currentTarget;if(L(null),_(""),K(!1),(null===t||void 0===t?void 0:t.files)&&(null===t||void 0===t?void 0:t.files.length)>0){var a=t.files[0];L(a),K(!0)}}})]})]}),Object(S.jsx)(p.a,{className:ie.inputWrapper,children:Object(S.jsx)(h.a,{size:"small",variant:"standard",disabled:!ne,InputProps:{readOnly:!0},value:null!==J?J.name:""})}),Object(S.jsxs)(p.a,{sx:{minWidth:"100px"},children:[Object(S.jsx)(x.a,{children:"Choose Language"}),Object(S.jsxs)(m.a,{size:"small",displayEmpty:!0,value:U,disabled:!ce,onChange:function(e){_(e.target.value)},children:[Object(S.jsx)(f.a,{value:"",children:Object(S.jsx)("em",{children:"None"})}),Object(S.jsx)(f.a,{value:"en",children:"En"}),Object(S.jsx)(f.a,{value:"ru",children:"Ru"})]})]}),Object(S.jsxs)(p.a,{children:[Object(S.jsx)(O.a,{variant:"contained",disabled:!re,onClick:te,className:ie.button,children:"Process"}),E&&Object(S.jsx)(v.a,{size:24,className:ie.loader})]})]}),""!==a&&Object(S.jsxs)(g.a,{variant:"outlined",className:ie.paper,children:[Object(S.jsx)(b.a,{className:ie.box,children:Object(S.jsx)("audio",{controls:!0,src:T,className:ie.audio})}),Object(S.jsx)(b.a,{className:ie.box,children:Object(S.jsxs)(u.a,{variant:"body1",gutterBottom:!0,children:[Object(S.jsx)("strong",{children:"Text:"})," ",a]})}),Object(S.jsx)(b.a,{children:Object(S.jsxs)(u.a,{variant:"body2",children:[Object(S.jsx)("strong",{children:"Keywords:"})," ",i]})})]}),Object(S.jsx)(w.a,{open:$,message:V,onClose:function(e,t){"clickaway"!==t&&ee(!1)},autoHideDuration:3e3})]})})};s.a.render(Object(S.jsx)(c.a.StrictMode,{children:Object(S.jsx)(B,{})}),document.getElementById("root"))}},[[97,1,2]]]);
//# sourceMappingURL=main.e3cd66bb.chunk.js.map