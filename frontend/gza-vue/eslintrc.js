module.exports = {
	parser: 'babel-eslint',
	parserOptions: {
		sourceType: 'module'
		ecmaFeatures: {
			experimentalObjectRestSpread: true
		}
	},
	extends: [
		'plugin:vue/recommended'
	],
	rules: {
		"comma-dangle": 0,
		"no-unused-vars": "warn",
		"no-console": 1,
		"no-mixed-spaces-and-tabs": 0,
		"no-unexpected-multiline": "warn"
	}
}