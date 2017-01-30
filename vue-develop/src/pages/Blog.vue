<template>
<div class="blog" :style="{height:blogH}" @click="hide = true" v-loading="loading" element-loading-text="正在提交,请稍等">
	<textarea class="content" v-model="formData.content" spellcheck="false"></textarea>
	<div class="html" v-html="markedHtml"></div>
	<div class="markTit" :class="{hide:hide}">Markdown</div>
	<div class="htmlTit" :class="{hide:hide}">HTML</div>
	<el-card class="card" v-bind:body-style="cardStyle" v-bind:class="{toLeft: !toLeft}">
		<input class="title" v-model="formData.title" placeholder="在此填写标题">
		<textarea class="description" maxlength="50" placeholder="在此填写文章描述" v-model="formData.description"></textarea>
		<div class="tags">
			<el-select class="tagSelect" v-model="formData.tag" multiple filterable allow-create placeholder="请选择或新增文章标签">
				<el-option v-for="item in tags" :value="item"></el-option>
			</el-select>
		</div>
		<el-button class="button right" type="primary" @click="postMessage">提交此篇文章</el-button>
		<el-button class="button left" type="text" @click="toLeft = false">收起标题</el-button>
	</el-card>
	<el-switch class="switch" v-model="toLeft" on-color="#324057" on-text="标题" off-text="标题"></el-switch>
</div>
</template>

<script>
import marked from 'marked'
import highlight from 'highlight'
export default {
	data(){
		return {
			blogH : "90%",
			blogId : null,
			hide : false,
			toLeft : true,
			//默认标签分类
			tags : ["python","javascript","html","css","markdown","sublime"],
			//表单提交时loading
			loading : false,
			//表单信息
			formData: {
				content : '',
				title : '',
				tag : [],
				description : ''
			},
			cardStyle : { 
				padding: '25px 16px 16px' , 
				width: '500px' ,
				height: '100px'
			}
		}
	},
	created: function () {
		this.blogId = this.$route.query.blogId
		marked.setOptions({
			highlight: function (code) {
				return highlight.highlightAuto(code).value
			}
		})
		this.setHeight
		window.onresize = function(){
			this.blogH = this.setHeight
		}
		this.getMessage()
	},
	computed : {
		markedHtml : function(){
			return marked(this.formData.content)
		}
	},
	methods : {
		//get编辑的blog的信息
		getMessage : function(){
			if(this.blogId || this.blogId === 0){
				this.loading = true
				this.ajax(this.setAjax("blog",{id : this.blogId},this.success,this.fail))
			}
		},
		//发送登录请求
		postMessage : function(){
			this.loading = true
			if(this.blogId || this.blogId === 0){
				this.ajax(this.setAjax("blogEdit",this.formData,this.success,this.fail))
			}else{
				this.ajax(this.setAjax("blogCreate",this.formData,this.success,this.fail))
			}
		},
		//表单验证
		submitForm : function(formName) {
			
		},
		//提交成功
		success : function(res){
			this.$router.push('/')
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
	position relative
.markTit
.htmlTit
	font-size 70px
	font-weight bold
	position absolute
	top 50%
	z-index 2
.markTit
	left 25%
	transform translate(-50%,-50%)
.htmlTit
	right 25%
	transform translate(50%,-50%)
textarea.content
.html
	width 50%
	height 100%
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
.card
	position absolute
	top 2%
	left 50%
	z-index 3
	transform translateX(-50%)
	transition left .8s
.button
	margin 10px
.title
	border none
	border-bottom 1px solid #324057
	width 100%
	font-size 20px
	color #324057
	padding 0
	margin-bottom 10px
	padding-bottom 5px
textarea.description
	width 100%
	height 60px
	padding 10px
	border 1px solid #ccc
.tags
	width 100%
	margin 10px 0
	height 60px
.tagSelect
	display block
	margin 0 auto
	overflow hidden
.switch
	position absolute
	top 2%
	right 2%
.toLeft
	left -50%
</style>
