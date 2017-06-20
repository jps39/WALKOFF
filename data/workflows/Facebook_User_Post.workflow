<?xml version="1.0" ?>
<workflows>
	<workflow name="facebookUserPostWorkflow">
		<options>
			<enabled>true</enabled>
			<scheduler autorun="false" type="cron">
				<sDT>2016-1-1 12:00:00</sDT>
				<interval>0.1</interval>
				<eDT>2016-3-15 12:00:00</eDT>
			</scheduler>
		</options>
		<start>2</start>
		<steps>
			<step id="2">
				<id>2</id>
				<app>FacebookUserPost</app>
				<action>post to wall</action>
				<position>
					<x>425</x>
					<y>282</y>
				</position>
				<inputs>
					<message>Explore WALKOFF at https://github.com/iadgov/WALKOFF :D :D :D</message>
				</inputs>
			</step>
		</steps>
	</workflow>
</workflows>
