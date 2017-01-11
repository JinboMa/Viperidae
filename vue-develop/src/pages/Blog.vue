<template lang="pug">
.blog
	textarea(v-model="markText")
	.html(v-html="markedHtml")
</template>

<script>
import marked from 'marked'
import highlight from 'highlight'
export default {
	data(){
		return {
			markText : ""
		}
	},
	created: function () {
		marked.setOptions({
			highlight: function (code) {
				return highlight.highlightAuto(code).value;
			}
		});
	},
	computed : {
		markedHtml : function(){
			return marked(this.markText)
		}
	},
	methods : {
		postMessage : function(){
			this.ajax({
				method : "GET",
				url : "login",
				formData : this.formData,
				successMsg : "登录成功",
				success : this.success,
				failMsg : "登录失败",
				fail : this.fail
			})
		},
		//提交成功
		success : function(res){
			this.$router.push({ path: '/', query: { nickname : this.formData.nickname }})
		},
		//提交失败
		fail : function(res){
			console.log("失败")
		}
	}
}
</script>

<style scoped lang="stylus">
.blog
	width 100%
	height 90%
	background gray
textarea
.html
	width 50%
	height 90%
	overflow scroll
	float left
	background #f6f6f6
	padding 20px
	font-family "Inconsolata", "Monaco", "Andale Mono", "Lucida Console", "Bitstream Vera Sans Mono", "Courier New", Courier, monospace
	font-size 14px
	line-height 1.55em
	white-space pre
textarea
	border none
	border-right 1px solid #ccc
	resize none
</style>
