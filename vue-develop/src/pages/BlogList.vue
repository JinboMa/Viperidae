<template lang="jade">
.blogList.content(v-loading="loading",element-loading-text="正在请求,请稍等")
	el-col(:span="12",v-for="(blog,item) in formData")
		blog-content(:blogMsg="blog",:blogId="item",@resetBlogList="getMessage")
	el-button.addBlog(type="info",@click="toAddBlog") 新建
	el-button.editAllBlog(type="info",@click="isEdit=true") 编辑
	el-dialog(title="编辑我的文章",v-model="isEdit")
		edit-blogs(:blogs="formData",:isEdit="isEdit",@changeDels="changeDels($event)")
		.dialog-footer(slot="footer")
			span.left.prompt 点击选择要删除的文章
			el-button(@click="isEdit=false") 取 消
			el-button(@click="postDelBlogs") 确 定
</template>
<script>
import BlogContent from '../components/BlogContent'
import EditBlogs from '../components/EditBlogs'
export default {
	data(){
		return {
			loading : false,
			formData : {
			},
			isEdit : false,
			delBlogs : []
		}
	},
	components : {
		BlogContent,
		EditBlogs
	},
	created : function(){
		this.getMessage()
	},
	methods : {
		//发送获取博客列表请求
		getMessage(){
			this.loading = true
			this.ajax(this.setAjax("blogList",{},this.success,this.fail))
		},
		//获取成功
		success(res){
			this.formData = JSON.parse(JSON.stringify(res))
		},
		//获取失败
		fail(res){
			console.log("失败",res)
		},
		changeDels(value){
			this.delBlogs = value
		},
		postDelBlogs(){
			this.$confirm('确定要删除所选文章么?', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
				type: 'warning'
			}).then(() => {
				this.ajax(this.setAjax("blogDelete",{list:this.delBlogs},this.delSuccess,this.delFail))
			}).catch(() => {
				this.$message({
					type: 'info',
					message: '已取消删除'
				});
			});
		},
		delSuccess(res){
			this.delBlogs = []
			this.getMessage()
			this.isEdit = false
		},
		delFail(res){
			console.log('失败',res)
		},
		toAddBlog(){
			this.$router.push({ path: 'Blog'})
		}
	}
}
</script>

<style scoped lang="stylus">
.blogList
	position relative
	padding-top 20px
.addBlog
.editAllBlog
	position absolute
	right -90px
.addBlog
	top 20px
.editAllBlog
	top 60px
</style>
