<template>
<div class="blogList content" v-loading="loading" element-loading-text="正在提交,请稍等">
	<el-row>
		<el-col :span="12">
			<blog-content v-for="blog in formData" :blogMsg="blog"></blog-content>
		</el-col>
	</el-row>
</div>
</template>

<script>
import BlogContent from '../components/BlogContent'
export default {
	data(){
		return {
			loading : false,
			formData : [
				{
					title : "title,标题,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : "3.7",
					author : "马金博",
					createTime : "2017-01-30 14:57"
				},
				{
					title : "title1,标题",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : "3.7",
					author : "马金博",
					createTime : "2017-01-30 14:57"
				},
				{
					title : "title2,标题",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : "3.7",
					author : "马金博",
					createTime : "2017-01-30 14:57"
				}
			]
		}
	},
	components : {
		BlogContent
	},
	methods : {
		//发送登录请求
		postMessage : function(){
			this.loading = true
			this.ajax(this.setAjax("blogList",this.formData,this.success,this.fail))
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
.blogList
	padding-top 20px
</style>
