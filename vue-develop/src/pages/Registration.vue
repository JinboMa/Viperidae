<template lang="pug">
.registration
	el-card.box-card(v-loading="loading" element-loading-text="正在注册")
		.logo 注 册
		el-form(v-bind:model="formData" v-bind:rules="rules" ref="regForm")
			el-form-item(label="手机号" prop="telphone")
				el-input(v-model="formData.telphone" placeholder="手机号")
			el-form-item(label="用户名" prop="nickname")
				el-input(v-model="formData.nickname" placeholder="昵称")
			el-form-item(label="密码" prop="password")
				el-input(v-model="formData.password" type="password" placeholder="6-20位")
			el-form-item
				el-button.regBtn(type="success" @click="submitForm('regForm')" size="large") 注 册
				router-link.login(to="/Login") 登录
</template>

<script>
export default {
	data(){
		return {
			//表单提交时loading
			loading : false,
			//表单信息
			formData: {
				telphone : '',
				nickname : '',
				password : ''
			},
			//表单规则
			rules: {
				nickname: [
				{ required: true, message: '请输入昵称', trigger: 'blur' },
				],
				telphone: [
				{ required: true, message: '请输入手机号', trigger: 'blur' },
				{ min: 11,max: 11, message: '请输入正确的手机号', trigger: 'blur' }
				],
				password: [
				{ required: true, message: '请输入密码', trigger: 'blur' },
				{ min: 6, max: 20, message: '密码长度在 6 到 20 个字符', trigger: 'blur' }
				]
			}
		}
	},
	methods: {
		//发送登录请求
		postMessage : function(){
			this.ajax(this.setAjax("registration",this.formData,this.success,this.fail))
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
		//请求成功函数
		success : function(res){
			this.$router.push({ path: '/', query: { nickname : this.formData.nickname }})
		},
		//请求失败
		fail : function(res){
			console.log("失败")
		}
	}
}
</script>

<style scoped lang="stylus">
$width = 350px
.registration
	font-weight bold
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
	height 26px
	font-weight bold
	font-size 30px
	font-family "Microsoft YaHei",sans-serif
	text-align center
	transform translateY(-20px)
	color #324057
.regBtn
	width 150px
	font-size 18px
	font-family "Microsoft YaHei",sans-serif
	font-weight bold
	display block
	margin 20px auto 0
.login
	font 12px normal
	color #3182bd
	cursor pointer
	position absolute
	right 5px
	bottom 0
	&:hover
		text-decoration underline
</style>
