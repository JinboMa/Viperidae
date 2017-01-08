<template lang="pug">
.login
	el-card.box-card(v-loading="loading" element-loading-text="正在登录")
		.logo LOGO
		el-form(v-bind:model="formData" v-bind:rules="rules" ref="loginForm")
			el-form-item(label="手机号" prop="telphone")
				el-input(v-model="formData.telphone")
			el-form-item(label="密码" prop="password")
				el-input(v-model="formData.password" type="password")
				a.forget 忘记密码
			el-form-item
				el-button.loginBtn(type="success" @click="submitForm('loginForm')" size="large") 登 录
				router-link.signIn(to="/Registration") 注册
</template>

<script>
export default {
	data(){
		return {
			//表单提交时loading
			loading : false,
			//表单信息
			formData: {
				telphone: '',
				password: ''
			},
			//表单规则
			rules: {
				telphone: [
				{ required: false, message: '请输入手机号', trigger: 'blur' },
				{ min: 11,max: 11, message: '请输入正确的手机号', trigger: 'blur' }
				],
				password: [
				{ required: false, message: '请输入密码', trigger: 'blur' },
				{ min: 6, max: 20, message: '密码长度在 6 到 20 个字符', trigger: 'blur' }
				]
			}
		}
	},
	methods : {
		//发送登录请求
		postMessage : function(){
			this.ajax({
				method : "POST",
				url : "login",
				formData : this.formData,
				option : 1,
				successMsg : "登录成功",
				success : this.success,
				failMsg : "登录失败",
				fail : this.fail
			})
		},
		//表单验证
		submitForm : function(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.loading = true
					this.postMessage()
				} else {
					this.$message.error("请正确填写数据")
				}
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
$width = 350px
.login
	width $width
	position absolute
	top 50%
	left 50%
	transform translate(-50%,-50%)
.box-card
	width $width
	height (@width+100)
	padding (@width/17.5) (@width/14)
.logo
	height 120px
	font-weight bold
	font-size 50px
	font-family "Microsoft YaHei",sans-serif
	text-align center
	color #324057
.loginBtn
	width 150px
	font-size 18px
	font-family "Microsoft YaHei",sans-serif
	font-weight bold
	display block
	margin 20px auto 0
.forget
.signIn
	font 12px normal
	color #3182bd
	cursor pointer
	&:hover
		text-decoration underline
.forget
	position absolute
	top 10px
	right 0
.signIn
	position absolute
	right 5px
	bottom 0
</style>
