<template lang="jade">
.editBlogs
	.item(v-for="(blog,id) in blogs",@click="toggle(id)")
		i.el-icon-delete.select(v-show="isCheck(id)")
		span.author {{blog.author}}
		span.time {{blog.time}}
		span.title(:title="blog.title") {{blog.title}}
</template>
<script>
export default{
	props:['blogs','isEdit'],
	data(){
		return{
			delBlogs : [],
			selectAll : false
		}
	},
	watch:{
		'delBlogs':function(value){
			this.$emit('changeDels',value)
		},
		'isEdit':function(){
			this.delBlogs = []
		}
	},
	methods:{
		isCheck(id){
			return (this.delBlogs.indexOf(id) != -1)
		},
		toggle(id){
			var isChose = this.isCheck(id)
			if(isChose){
				var index = this.delBlogs.indexOf(id)
				this.delBlogs.splice(index, 1)
			}else{
				this.delBlogs.push(id)
			}
		}
	}
}
</script>
<style scoped lang="stylus">
.editBlogs
	max-height 400px
	overflow auto
.item
	cursor pointer
	padding 5px
	border-bottom 1px solid #ccc
	width 400px
	overflow hidden
	text-overflow ellipsis
	white-space nowrap
	margin 0 auto
.select
.author
.time
	margin-right 5px
.author
	color #1F2D3D
	font-weight bolder
.time
	color #F7BA2A
	font-weight bolder
.title
	color #20A0FF
	font-weight bolder
.select
	color red
	float right
.selectAll
	float right
	font-size 12px
</style>