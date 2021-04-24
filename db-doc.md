# Db Documentation

## Abreviations

ou
: over under
	

Tables:

	GameMatchup

	Free Pick

	Handicapper

### Sport League Enum

	NBA, MLB, NFL, NHL

# Tables

## GameMatchup

	|---------------|---------------------------------------|
	| field 		| description (optional)				|
	|---------------|---------------------------------------|
	| id			|										|
	|---------------|---------------------------------------|
	| sport			| sport type enum 						|
	|---------------|---------------------------------------|
	| homeTeam		|										|
	|---------------|---------------------------------------|
	| awayTeam		|										|
	|---------------|---------------------------------------|
	| gameTime		|										|
	| openOU		| straight from covers matchups page    |
	| liveOU		| will be updated from various sources  |
	|				| still need to determine when/where	|
	| openHomeOdds	| straight from covers matchups page	|
	|---------------|---------------------------------------|
	| homeConsensus	| just get the string on each side		|
	| 					is composed e.x. X% -X/+X/-XXX		|
	| awayConsensus											|
	|---------------|---------------------------------------|



	|---------------|---------------------------------------|
	| field 		| description (optional)				|
	|---------------|---------------------------------------|
	| id			|										|
	| sport			| sport type enum 						|
	| homeTeam		|										|
	| awayTeam		|										|
	|===============|=======================================|
	| gameTime		|										|
	| openOU		| straight from covers matchups page    |
	| liveOU		| will be updated from various sources  |
	|				| still need to determine when/where	|
	| openHomeOdds	| straight from covers matchups page	|
	|---------------|---------------------------------------|
	|---------------|---------------------------------------|
	| homeConsensus	| just get the string on each side		|
	| 					is composed e.x. X% -X/+X/-XXX		|
	| awayConsensus											|
	|---------------|---------------------------------------|


	|---------------|---------------------------------------|
	| 			Was an idea... not implemented				|
	|---------------|---------------------------------------|
	| ~~liveHomeOdds~~										|
	| ~~liveAwayOdds~~										|
	|---------------|---------------------------------------|


## Free Pick

	|---------------|---------------------------------------|
	| field 		| description 							|
	|---------------|---------------------------------------|
	| id			|										|
	|---------------|---------------------------------------|
	| theFix 		| the actual pick						|
	|---------------|---------------------------------------|
	| Handicapper	|										|
	|---------------|---------------------------------------|


## Handicapper

	|---------------|---------------------------------------|
	| field 		| description 							|
	|---------------|---------------------------------------|
	| id			|										|
	|---------------|---------------------------------------|
	| name			|										|
	|---------------|---------------------------------------|
	| last10		|										|
	|---------------|---------------------------------------|
	| sportRecord	| draws one to many realtionship between|
	|				| sport record a handicapper			|
	|     			| will a record for each sport			|
	|---------------|---------------------------------------|
	| freePicks		| draws one to many realtionship between|
	|				| a handicapper will give free picks	|
	|---------------|---------------------------------------|
