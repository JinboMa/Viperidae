webpackJsonp([2,0],[function(e,t,n){"use strict";function a(e){return e&&e.__esModule?e:{default:e}}var o=n(3),r=a(o),s=n(70),i=a(s),l=n(83),u=a(l),d=n(82),c=a(d),f=n(52),p=a(f);n(63);var m=n(73),v=a(m),_=n(74),h=a(_),g=n(75),x=a(g);r.default.use(u.default),r.default.use(c.default),r.default.http.options.emulateJSON=!0,r.default.use(p.default),new r.default({el:"#app",router:new u.default({mode:"history",routes:[{path:"/",component:v.default},{path:"/Login",component:h.default},{path:"/Registration",component:x.default}]}),template:"<App/>",components:{App:i.default}}),r.default.prototype.ajax=function(e,t,n,a){1==n&&(n={headers:{"Content-Type":"x-www-from-urlencoded"}}),this.$http.post(e,t,n).then(function(e){console.log(e)})},r.default.prototype.setTime=function(e){}},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(e,t,n){"use strict";function a(e){return e&&e.__esModule?e:{default:e}}Object.defineProperty(t,"__esModule",{value:!0});var o=n(71),r=a(o),s=n(72),i=a(s);t.default={name:"app",components:{MyHeader:r.default,PutTop:i.default},methods:{},data:function(){return{}}}},function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{}}}},function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{}}}},function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{}}}},function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{formData:{telphone:"",password:""}}},methods:{postMessage:function(){this.ajax("http://120.26.100.13:8088/login",this.formData,1)},postBack:function(e){console.log(e)}}}},function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{formData:{telphone:"",nickname:"",password:""},rules:{nickname:[{required:!0,message:"请输入昵称",trigger:"blur"}],telphone:[{required:!0,message:"请输入手机号",trigger:"blur"},{min:11,max:11,message:"请输入正确的手机号",trigger:"change"}],password:[{required:!0,message:"请输入密码",trigger:"blur"},{min:6,max:20,message:"密码长度在 6 到 20 个字符",trigger:"change"}]}}},methods:{postMessage:function(){this.ajax("http://120.26.100.13:8088/registration",this.formData,1)},postBack:function(e){console.log(e.response.result)}}}},,,,,,,,,,,,,,,,function(e,t){},function(e,t){},function(e,t){},function(e,t){},function(e,t){},function(e,t){},function(e,t){},function(e,t,n){var a,o;n(69),a=n(42);var r=n(81);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,e.exports=a},function(e,t,n){var a,o;n(67),a=n(43);var r=n(79);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,o._scopeId="data-v-a9c4385c",e.exports=a},function(e,t,n){var a,o;n(66),a=n(44);var r=n(78);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,o._scopeId="data-v-8942b402",e.exports=a},function(e,t,n){var a,o;n(68),a=n(45);var r=n(80);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,o._scopeId="data-v-d598c326",e.exports=a},function(e,t,n){var a,o;n(64),a=n(46);var r=n(76);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,o._scopeId="data-v-5edb4184",e.exports=a},function(e,t,n){var a,o;n(65),a=n(47);var r=n(77);o=a=a||{},"object"!=typeof a.default&&"function"!=typeof a.default||(o=a=a.default),"function"==typeof o&&(o=o.options),o.render=r.render,o.staticRenderFns=r.staticRenderFns,o._scopeId="data-v-6a61bd24",e.exports=a},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"login"},[n("el-card",{staticClass:"box-card"},[n("div",{staticClass:"logo"},[e._v("LOGO")]),n("el-form",{attrs:{model:e.formData}},[n("el-form-item",{attrs:{label:"手机号"}},[n("el-input",{directives:[{name:"model",rawName:"v-model",value:e.formData.telphone,expression:"formData.telphone"}],domProps:{value:e.formData.telphone},on:{input:function(t){e.formData.telphone=t}}})],1),n("el-form-item",{attrs:{label:"密码"}},[n("el-input",{directives:[{name:"model",rawName:"v-model",value:e.formData.password,expression:"formData.password"}],attrs:{type:"password"},domProps:{value:e.formData.password},on:{input:function(t){e.formData.password=t}}}),n("a",{staticClass:"forget"},[e._v("忘记密码")])],1),n("el-form-item",[n("el-button",{staticClass:"loginBtn",attrs:{type:"success",size:"large"},on:{click:e.postMessage}},[e._v("登 录")]),n("router-link",{staticClass:"signIn",attrs:{to:"/Registration"}},[e._v("注册")])],1)],1)],1)],1)},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"registration"},[n("el-card",{staticClass:"box-card"},[n("div",{staticClass:"logo"},[e._v("注 册")]),n("el-form",{attrs:{model:e.formData,rules:e.rules}},[n("el-form-item",{attrs:{label:"手机号",prop:"telphone"}},[n("el-input",{directives:[{name:"model",rawName:"v-model",value:e.formData.telphone,expression:"formData.telphone"}],attrs:{placeholder:"手机号"},domProps:{value:e.formData.telphone},on:{input:function(t){e.formData.telphone=t}}})],1),n("el-form-item",{attrs:{label:"用户名",prop:"nickname"}},[n("el-input",{directives:[{name:"model",rawName:"v-model",value:e.formData.nickname,expression:"formData.nickname"}],attrs:{placeholder:"昵称"},domProps:{value:e.formData.nickname},on:{input:function(t){e.formData.nickname=t}}})],1),n("el-form-item",{attrs:{label:"密码",prop:"password"}},[n("el-input",{directives:[{name:"model",rawName:"v-model",value:e.formData.password,expression:"formData.password"}],attrs:{type:"password",placeholder:"6-20位"},domProps:{value:e.formData.password},on:{input:function(t){e.formData.password=t}}})],1),n("el-form-item",[n("el-button",{staticClass:"regBtn",attrs:{type:"success",size:"large"},on:{click:e.postMessage}},[e._v("注 册")]),n("router-link",{staticClass:"login",attrs:{to:"/Login"}},[e._v("登录")])],1)],1)],1)],1)},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"putTop"})},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"myHeader"},[n("el-menu",{staticClass:"el-menu-demo",attrs:{theme:"dark","default-active":"1",mode:"horizontal"}},[n("el-menu-item",{attrs:{index:"1"}},[n("i",{staticClass:"el-icon-menu"})]),n("el-submenu",{attrs:{index:"2"}},[n("template",{slot:"title"},[e._v("生活")]),n("el-menu-item",{attrs:{index:"2-1"}},[e._v("工作列表")]),n("el-menu-item",{attrs:{index:"2-2"}},[e._v("生活列表")]),n("el-menu-item",{attrs:{index:"2-3"}},[e._v("其他列表")])],2),n("el-submenu",{attrs:{index:"3"}},[n("template",{slot:"title"},[e._v("社交")]),n("el-menu-item",{attrs:{index:"2-1"}},[e._v("我的朋友圈")]),n("el-menu-item",{attrs:{index:"2-2"}},[e._v("我的微博")]),n("el-menu-item",{attrs:{index:"2-3"}},[e._v("我的QQ空间")])],2),n("el-menu-item",{attrs:{index:"4"}},[e._v("直播")]),n("el-menu-item",{attrs:{index:"5"}},[e._v("聊天")]),n("el-menu-item",{attrs:{index:"6"}},[e._v("设置")]),n("el-menu-item",{staticClass:"time",staticStyle:{float:"right"},attrs:{index:"0"}},[e._v("2017/1/7 12：30")])],1)],1)},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"index"},[n("router-link",{attrs:{to:"/Login"}},[e._v("登录")]),n("router-link",{attrs:{to:"/Registration"}},[e._v("注册")])],1)},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("my-header"),n("put-top"),n("router-view")],1)},staticRenderFns:[]}}]);
//# sourceMappingURL=app.c24352ab0c8ff25af5ac.js.map