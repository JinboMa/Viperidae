<template lang="jade">
router-link.blogContent(:to="{ path: 'Blog', query: { blogId: blogId }}")
	.authorMsg
		img(:src="blogMsg.authorImg")
		span.author {{blogMsg.author}}
		span.createTime {{blogMsg.createTime}}
		el-rate.rate(v-model="blogMsg.rate",disabled,show-text,text-color="#ff9900")
	h3 {{blogMsg.title}}
	p {{blogMsg.description}}
</template>
<script>
export default {
	props : ["blogMsg","blogId"]
}
</script>

<style scoped lang="stylus">
.blogContent
	display block
	width 100%
	border-bottom 1px solid #f0f0f0
	padding 20px
	cursor pointer
	&:hover
		box-shadow 0 0 5px #20A0FF
.authorMsg
	margin-bottom 10px
.authorMsg img
	vertical-align middle
	width 32px
	height @width
	border-radius 50%
	border 1px solid #ddd
.author
	color #333
	font-size 13px
	padding-left 3px
.createTime
	font-size 13px
	color #969696
	padding-left 3px
h3
	width 70%
	overflow hidden
	text-overflow ellipsis
	white-space nowrap
	font-size 18px
	color #969696
	font-weight 700
	margin-bottom 5px
.rate
	display inline-block
	vertical-align middle
	transform scale(0.7,0.7) translateX(-15px)
p
	width 100%
	display -webkit-box
	-webkit-box-orient vertical
	-webkit-line-clamp 1
	overflow hidden
	font-size 13px
</style>
