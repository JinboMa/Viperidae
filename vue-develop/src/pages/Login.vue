<template lang="jade">
.login
	el-card.box-card(v-loading="loading",element-loading-text="正在登录")
		.logo LOGO
		el-form(:model="formData",:rules="rules",ref="loginForm")
			el-form-item(label="用户名",prop="username")
				el-input(v-model="formData.username" placeholder="用户名/手机号/邮箱")
			el-form-item(label="密码",prop="password")
				el-input(v-model="formData.password",type="password")
				a.forget 忘记密码
			el-form-item
				el-button.loginBtn(type="success",@click="submitForm('loginForm')",size="large") 登 录
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
				username: '',
				password: ''
			},
			//表单规则
			rules: {
				username: [
				{ required: false, message: '请输入用户名', trigger: 'blur' }
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
			this.ajax(this.setAjax("login",this.formData,this.success,this.fail))
		},
		//表单验证
		submitForm : function(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.loading = true
					this.postMessage()
				} else {
					this.$message.error("请正确填写用户名和密码")
				}
			})
		},
		//提交成功
		success : function(res){
			localStorage.setItem('token',res.token)
			localStorage.setItem('username',res.username)
			this.$emit('login')
			this.$router.go(-1)
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
