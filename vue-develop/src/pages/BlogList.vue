<template>
<div class="blogList content" v-loading="loading" element-loading-text="正在请求,请稍等">
	<el-row>
		<el-col :span="12">
			<blog-content v-for="(blog,item) in formData" :blogMsg="blog" :blogId="item"></blog-content>
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
			formData : {
				5:{
					title : "title,标题,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow,test overflow",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : 3.7,
					author : "马金博",
					createTime : "2017-01-30 14:57"
				},
				2:{
					title : "title1,标题",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : 3.7,
					author : "马金博",
					createTime : "2017-01-30 14:57"
				},
				3:{
					title : "title2,标题",
					description : "test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ;test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz ; test content,test length for 100,abcdefg higklmn opqrst uvwxyz,abcdefg hijklmn opqrst uvwxyz",
					rate : 3.7,
					author : "马金博",
					createTime : "2017-01-30 14:57"
				}
			}
		}
	},
	components : {
		BlogContent
	},
	created : function(){
		this.getMessage()
	},
	methods : {
		//发送获取博客列表请求
		getMessage : function(){
			this.loading = true
			this.ajax(this.setAjax("blogList",this.formData,this.success,this.fail))
		},
		//获取成功
		success : function(res){
			this.formData = res.message
		},
		//获取失败
		fail : function(res){
			console.log("失败",res)
		}
	}
}
</script>

<style scoped lang="stylus">
.blogList
	padding-top 20px
</style>
