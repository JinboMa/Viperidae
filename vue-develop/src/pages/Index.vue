<template lang="pug">
.index
	router-link(to="/Login") 登录
	router-link(to="/Registration") 注册
	el-button(type="primary" @click="postMessage") test
</template>

<script>
export default {
	data(){
		return {
			formData : {
				tel : 13091719000
			}
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
</style>
