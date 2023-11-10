from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection

orchestrator_connection = OrchestratorConnection.create_connection_from_args()

orchestrator_connection.log_info("Hello World!")

args = orchestrator_connection.process_arguments
orchestrator_connection.log_info(args)
