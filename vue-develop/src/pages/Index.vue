<template>
	<div class="index">
		<el-popover ref="popover4" placement="bottom" width="400" trigger="hover">
			
		</el-popover>
		<el-button v-popover:popover4>click 激活</el-button>
	</div>
</template>

<script>
	export default {
		data(){
			return {
				Info : "欢迎来到主页，新用户请点击注册！",
				gridData: [{
					date: '2016-05-02',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}, {
					date: '2016-05-04',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}, {
					date: '2016-05-01',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}, {
					date: '2016-05-03',
					name: '王小虎',
					address: '上海市普陀区金沙江路 1518 弄'
				}]
			}
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
