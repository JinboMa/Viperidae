<template lang="pug">
	#app
		my-header
		put-top
		router-view
</template>

<script>
import MyHeader from './components/MyHeader'
import PutTop from './components/PutTop'

export default {
	name: 'app',
	components: {
		MyHeader,
		PutTop
	},
	methods: {
		
	},
	data(){
		return {
			
		}
	}
}
</script>

<style lang="stylus">
*
	margin 0
	padding 0
	font-family "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif
div
	box-sizing border-box
a
	text-decoration none
</style>
