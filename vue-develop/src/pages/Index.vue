<template lang="pug">
.index
	p {{Info}}
</template>

<script>
export default {
	data(){
		return {
			Info : "欢迎来到主页，新用户请点击注册！"
		}
	},
	created: function () {
	},
	computed : {
	},
	methods : {
	}
}
</script>

<style scoped lang="stylus">
.index
	width 1050px
	position absolute
	top 50%
	left 50%
	transform translate(-50%,-50%)
p
	font-size 20px
	font-weight bold
	color #324057
	text-align center
</style>
