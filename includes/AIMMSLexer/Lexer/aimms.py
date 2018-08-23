# -*- coding: utf-8 -*-
"""
    pygments.lexers.aimms
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for the AIMMS language. <https://aimms.com/>

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import re
from pygments.lexer import RegexLexer, bygroups, using, this, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Token, Whitespace, Error

__all__ = ['AIMMSLexer']    


# Here is the regex to find every identifier declaration, used later on the get_tokens_unprocessed
id_re = re.compile(r'(?i)(Set|Calendar|Horizon|index|Parameter|ElementParameter|StringParameter|UnitParameter|Variable|elementvariable|complementarityvariable|Constraint|Arc|Node|uncertaintyvariable|uncertaintyconstraint|Activity|Resource|MathematicalProgram|Macro|Model|Assertion|DatabaseTable|DatabaseProcedure|File|Procedure|Function|Quantity|Convention|LibraryModule|Module|Section|Declaration|ExternalProcedure|File)(?:\s+)(\w+)(\s*\{|\s*;|\s*:)')

# Create new Tokens for main identifier types (Parameters,EP,SP,Set, Variable, Constraint, etc.)
Token.Name.Set
Token.Name.Parameter
Token.Name.StringParameter
Token.Name.ElementParameter
Token.Name.Variable
Token.Name.Constraint
Token.Name.MathematicalProgram
Token.Name.Quantity
Token.Name.DatabaseTable
Token.Name.Convention
Token.Name.Index
Token.Name.Procedure


def switcher(argument):
    Types = {
        "Set":Name.Set,
        "Parameter":Name.Parameter,
        "StringParameter":Name.StringParameter,
        "ElementParameter":Name.ElementParameter,
        "Variable":Name.Variable,
        "Constraint":Name.Constraint,
        "MathematicalProgram":Name.MathematicalProgram,
        "Quantity":Name.Quantity,
        "DatabaseTable":Name.DatabaseTable,
        "Convention":Name.Convention,
        "Procedure":Name.Procedure,
        "Index":Name.Index}

    return Types.get(argument, Name.Variable)


class AIMMSLexer(RegexLexer):
    """
    For AIMMS source code.

    .. versionadded:: 0.1
    """
    name = 'AIMMS'
    aliases = ['aimms']
    filenames = ['*.aimms','*.ams']

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text.Whitespace),
            
            #Comments inside procedures
            (r'!.*?\n', Comment.Single),
            (r'/[*](.|\n)*?[*]/', Comment.Multiline),
            
            #For AMS files, forces a Comment attribute block to be just a comment, nothing else, weather it is Comment: ... or Comment: {...}
            (r'(Comment:\s+{?)((.|\n)+?)([};])',bygroups(Name.Attribute, Comment.Multiline, Name.Attribute)),

            #For AMS files, matches all Attributes from any Identifier declaration
            (r'(\w+)(:)(\s+)', bygroups(Name.Attribute,Operator,Text.Whitespace)),
                      
            #For AMS Files, matches all function arguments pre formatted
            (r'(\b\w+)(\s+:\s+\b|\s+:\s+\B)', bygroups(Name.Argument, Text)),
            
            # AllKeywords: to be blue! # TODO: put this list outside
            (words(('Adjustable','affine','AIMMS','and','append','apply','arc','argmax','argmin','array','ASCII','assert','assertion','Atleast', 'Atmost','Automatic','backup','binary','Block','boolean','Bounded','bounds','Box','break','by','calendar','Chance','checking', 'cleandependents','cleanup','code','CoefficientRange','Coefficients','Coldim','ColsPerLine','Columns','comment','Complementarity', 'composite','constant','constraint','constraints','Contiguous','convention','conversions','ConvexHull','ConvexHullEx','COP','count', 'cross','CSP','data','database','decimals','declaration','default','definition','delta','dense','Dependency','device','direction', 'disk','display','Distribution','do','double','elementnumber','Ellipsoid','else','elseif','empty','EmptyElementAllowed','encoding', 'EndBlock','endfor','endfunction','endif','EndLibraryModule','endmodel','endmodule','endprocedure','endrepeat','endsection', 'endswitch','endwhile','error','exactly','exec','exists','FailCount','file','filedate','filtering','For','ForAll','fortran', 'FortranConventions','free','function','Gaussian','halt','handle','horizon','identifier','identifiers','if','in','inactive', 'IncludeInCutPool','IncludeInLazyConstraintPool','index','indicator','IndicatorConstraint','indices','inf','inline','inout','input', 'insert','integer','integer16','integer32','integer8','interface','Intersection','IsDiversificationFilter','IsRangeFilter','Level', 'levels','library','LibraryModule','loopcount','LP','LS','macro','main','mathematical','maximize','maxint','MCP','merge','method', 'minimize','MINLP','MIP','MIQCP','MIQP','mode','model','module','MPCC','na','NBest','negative','netinflow','netoutflow','network', 'NLP','NLS','node','nondefault','none','nonnegative','nonpositive','nosave','not','nth','off','on','onerror','only','onlyif', 'option','Optional','options','or','ordinalnumber','output','parallel','parameter','parameters','penalty','positive','prefix', 'procedure','prod','program','property','protected','public','put','putclose','putft','puthd','putpage','QCP','QP','quantity', 'raise','Random','raw','read','ReadOnly','Rebuild','ReducedCost','relation','repeat','replace','retainspecials','RetainsValue', 'return','RightHandSideRange','RMINLP','RMIP','Rowdim','Rows','section','semicontinuous','sequential','set','ShadowPrice', 'ShadowPriceRange','skip','solve','Sort','sos1','sos2','source','sparse','stochastic','string','subject','subset','suffix','sum', 'support','switch','Symmetric','table','tags','tensor','then','to','transitionOnlyNext','truncate','tuple','type','Uncertain', 'undf','Unicode','Unimodal','Union','unordered','update','user','UseResultSet','Utf8','ValueRange','variable','variables', 'violation','void','WarnOnly','when','where','while','window','with','work','write','xor','zero'), prefix=r'(?i)',suffix=r'\b'), Keyword.Reserved),
            
            # AllPredeclaredIdentifiers: to be red! # TODO: put this list outside
            (words(('Aimms_predefined','Predeclared_Identifiers','System_Settings_Related_Identifiers','AllSymbols','IndexSymbols', 'AllAimmsStringConstantElements','IndexAimmsStringConstantElements','AimmsStringConstants','AllOptions','IndexOptions', 'AllPredeclaredIdentifiers','IndexPredeclaredIdentifiers','AllKeywords','IndexKeywords','AllSolvers','IndexSolvers', 'AllGMPExtensions','IndexGMPExtensions','AllColors','IndexColors','AllCharacterEncodings','IndexCharacterEncodings', 'ASCIICharacterEncodings','IndexASCIICharacterEncodings','UnicodeCharacterEncodings','IndexUnicodeCharacterEncodings', 'ASCIIUnicodeCharacterEncodings','IndexASCIIUnicodeCharacterEncodings','AllAvailableCharacterEncodings', 'IndexAvailableCharacterEncodings','AllAuthorizationLevels','IndexAuthorizationLevels','CurrentAuthorizationLevel','CurrentUser', 'CurrentGroup','ProfilerData','CurrentSolver','CurrentDefaultCaseType','Language_Related_Identifiers','AggregationTypes', 'IndexAggregationTypes','AllAttributeNames','IndexAttributeNames','AllColumnTypes','IndexColumnTypes','AllIdentifierTypes', 'IndexIdentifierTypes','AllIsolationLevels','IndexIsolationLevels','AllFileAttributes','IndexFileAttributes', 'AllDataColumnCharacteristics','IndexDataColumnCharacteristics','AllDatabaseInterfaces','IndexDatabaseInterfaces', 'AllDatasourceProperties','IndexDatasourceProperties','AllMathematicalProgrammingTypes','IndexMathematicalProgrammingTypes', 'AllMatrixManipulationDirections','IndexMatrixManipulationDirections','AllMatrixManipulationProgrammingTypes', 'IndexMatrixManipulationProgrammingTypes','AllRowColumnStatuses','IndexRowColumnStatusess','AllRowTypes','IndexRowTypes', 'AllMathematicalProgrammingRowTypes','IndexMathematicalProgrammingRowTypes','AllConstraintProgrammingRowTypes', 'IndexConstraintProgrammingRowTypes','AllSolutionStates','IndexSolutionStates','AllBasicValues','IndexBasicValues', 'AllChanceApproximationTypes','IndexChanceApproximationTypes','AllSolverInterrupts','IndexSolverInterrupts','AllExecutionStatuses', 'IndexExecutionStatus','AllStochasticGenerationModes','IndexStochasticGenerationModes','AllIntrinsics','IndexIntrinsics', 'AllProfilerTypes','IndexProfilerTypes','AllSuffixNames','IndexSuffixNames','AllDifferencingModes','IndexDifferencingModes', 'AllCaseComparisonModes','IndexCaseComparisonModes','AllValueKeywords','IndexValueKeywords','AllViolationTypes', 'IndexViolationTypes','ContinueAbort','IndexContinueAbort','DiskWindowVoid','IndexDiskWindowVoid','Integers','IndexIntegers', 'MaximizingMinimizing','IndexMaximizingMinimizing','CreatePresolvedLevels','IndexCreatePresolvedLevels','MergeReplace', 'IndexMergeReplace','DatabaseWriteModes','IndexDatabaseWriteModes','OnOff','IndexOnOff','TimeslotCharacteristics', 'IndexTimeslotCharacteristics','YesNo','IndexYesNo','Model_Related_Identifiers','AllAssertions','IndexAssertions','AllConstraints', 'IndexConstraints','AllConventions','IndexConventions','AllDatabaseTables','IndexDatabaseTables','AllDefinedParameters', 'IndexDefinedParameters','AllDefinedSets','IndexDefinedSets','AllFiles','IndexFiles','AllFunctions','IndexFunctions', 'AllGeneratedMathematicalPrograms','IndexGeneratedMathematicalPrograms','AllIdentifiers','IndexIdentifiers', 'SecondIndexIdentifiers','AllIndices','IndexIndices','AllIntegerVariables','IndexIntegerVariables','AllMacros','IndexMacros', 'AllMathematicalPrograms','IndexMathematicalPrograms','AllNonlinearConstraints','IndexNonlinearConstraints','AllParameters', 'IndexParameters','AllProcedures','IndexProcedures','AllQuantities','IndexQuantities','AllSections','IndexSections','AllSets', 'IndexSets','AllSolverSessionCompletionObjects','IndexSolverSessionCompletionObjects','AllSolverSessions','IndexSolverSessions', 'AllGMPEvents','IndexGMPEvents','AllStochasticParameters','IndexStochasticParameters','AllStochasticVariables', 'IndexStochasticVariables','AllStochasticConstraints','IndexStochasticConstraints','AllSubsetsOfAllIdentifiers', 'IndexSubsetsOfAllIdentifiers','AllUpdatableIdentifiers','IndexUpdatableIdentifiers','AllUncertainParameters', 'IndexUncertainParameters','AllUncertaintyConstraints','IndexUncertaintyConstraints','AllVariables','IndexVariables', 'AllVariablesConstraints','IndexVariablesConstraints','Execution_State_Related_Identifiers','AllProgressCategories', 'IndexProgressCategories','AllStochasticScenarios','IndexStochasticScenarios','CurrentAutoUpdatedDefinitions', 'IndexCurrentAutoUpdatedDefinitions','CurrentErrorMessage','CurrentFile','CurrentFileName','CurrentGeneratedMathematicalProgram', 'CurrentInputs','IndexCurrentInputs','CurrentPageNumber','CurrentMatrixBlockSizes','ODBCDateTimeFormat','CurrentMatrixRowCount', 'CurrentMatrixColumnCount','Case_Management_Related_Identifiers','AllCases','IndexCases','AllCaseTypes','IndexCaseTypes', 'AllDataCategories','IndexDataCategories','AllDataFiles','IndexDataFiles','AllDataSets','IndexDataSets','CurrentCase', 'CurrentCaseSelection','IndexCurrentCaseSelection','CurrentDataset','DataManagementMonitorID','CurrentCaseFileContentType', 'AllCaseFileContentTypes','IndexCaseFileContentTypes','CaseFileURL','Date_Time_Related_Identifiers','AllAbbrMonths', 'IndexAbbrMonths','AllAbbrWeekdays','IndexAbbrWeekdays','AllMonths','IndexMonths','AllTimeZones','IndexTimeZones','AllWeekdays', 'IndexWeekdays','LocaleAllAbbrMonths','LocaleIndexAbbrMonths','LocaleAllAbbrWeekdays','LocaleIndexAbbrWeekdays','LocaleAllMonths', 'LocaleIndexMonths','LocaleAllWeekdays','LocaleIndexWeekdays','LocaleLongDateFormat','LocaleShortDateFormat','LocaleTimeFormat', 'LocaleTimeZoneName','LocaleTimeZoneNameDST','ConstraintProgramming','cp','ErrorHandling','errh','errh::ErrorHandlingIdentifiers', 'errh::AllErrorSeverities','errh::IndexErrorSeverities','errh::AllErrorCategories','errh::IndexErrorCategories','errh::ErrorCodes', 'errh::IndexErrorCodes','errh::PendingErrors','errh::IndexPendingErrors'), prefix=r'\b(?i)', suffix=r'\b'), Name.Builtin),
            
            #Matches any string
            (r'\".*?\"', String.Double),
            (r'\'.*?\'', String.Single),
            
            #Matches any punctuation (parentheses, curly brackets, etc.)
            (r'[()\[\]{},;:]+', Punctuation),
             
            #AllIntrinsic functions: to be red! # TODO: put this list outside
            (words(('ActiveCard','Card','ConvertUnit','DistributionCumulative','DistributionDensity','DistributionDeviation', 'DistributionInverseCumulative','DistributionInverseDensity','DistributionKurtosis','DistributionMean','DistributionSkewness', 'DistributionVariance','Element','EvaluateUnit','First','FormatString','Last','Ord','Unit','Val','Aggregate', 'AttributeContainsString','AttributeLength','AttributeToString','callerLine','callerNode','callerAttribute', 'callerNumberOfLocations','CaseCompareIdentifier','CaseCreateDifferenceFile','CloseDataSource','cp::ActivityBegin', 'cp::ActivityEnd','cp::ActivityLength','cp::ActivitySize','cp::AllDifferent','cp::Alternative','cp::Span','cp::Synchronize', 'cp::BeginAtBegin','cp::BeginAtEnd','cp::BeginBeforeBegin','cp::BeginBeforeEnd','cp::EndAtBegin','cp::EndAtEnd', 'cp::EndBeforeBegin','cp::EndBeforeEnd','cp::BeginOfNext','cp::BeginOfPrevious','cp::EndOfNext','cp::EndOfPrevious', 'cp::LengthOfNext','cp::LengthOfPrevious','cp::SizeOfNext','cp::SizeOfPrevious','cp::GroupOfNext','cp::GroupOfPrevious', 'cp::BinPacking','cp::Cardinality','cp::Count','cp::Channel','cp::Lexicographic','cp::ParallelSchedule','cp::Sequence', 'cp::SequentialSchedule','CreateTimeTable','ConstraintVariables','ConvertReferenceDate','CloneElement','FileRead','FindNthString', 'FindReplaceNthString','FindReplaceStrings','FindString','StringOccurrences','RegexSearch','CurrentToMoment','CurrentToString', 'CurrentToTimeSlot','DaylightsavingEndDate','DaylightsavingStartDate','DeclaredSubset','DomainIndex','IndexRange', 'ListExpressionSubstitutions','LoadDatabaseStructure','DirectoryGetFiles','DirectoryGetSubdirectories','DirectSQL','Disaggregate', 'ElementCast','ElementRange','EnvironmentGetString','EnvironmentSetString','errh::Adapt','errh::Attribute','errh::Category', 'errh::Code','errh::Column','errh::CreationTime','errh::Filename','errh::InsideCategory','errh::IsMarkedAsHandled','errh::Line', 'errh::MarkAsHandled','errh::Message','errh::Multiplicity','errh::Node','errh::NumberOfLocations','errh::Severity', 'spreadsheet::AddNewSheet','spreadsheet::AssignParameter','spreadsheet::AssignSet','spreadsheet::AssignTable', 'spreadsheet::AssignValue','spreadsheet::ClearRange','spreadsheet::CloseWorkbook','spreadsheet::ColumnName', 'spreadsheet::ColumnNumber','spreadsheet::CopyRange','spreadsheet::CreateWorkbook','spreadsheet::DeleteSheet', 'spreadsheet::GetAllSheets','spreadsheet::Print','spreadsheet::RetrieveParameter','spreadsheet::RetrieveSet', 'spreadsheet::RetrieveTable','spreadsheet::RetrieveValue','spreadsheet::RunMacro','spreadsheet::SaveWorkbook', 'spreadsheet::SetActiveSheet','spreadsheet::SetOption','spreadsheet::SetUpdateLinksBehavior','spreadsheet::SetVisibility', 'FindUsedElements','GenerateCUT','GMP::Coefficient::Get','GMP::Coefficient::GetQuadratic','GMP::Coefficient::Set', 'GMP::Coefficient::SetMulti','GMP::Coefficient::SetQuadratic','GMP::Column::Add','GMP::Column::Delete','GMP::Column::Freeze', 'GMP::Column::FreezeMulti','GMP::Column::GetLowerbound','GMP::Column::GetName','GMP::Column::GetScale','GMP::Column::GetStatus', 'GMP::Column::GetType','GMP::Column::GetUpperbound','GMP::Column::SetAsObjective','GMP::Column::SetLowerbound', 'GMP::Column::SetLowerboundMulti','GMP::Column::SetType','GMP::Column::SetUpperbound','GMP::Column::SetUpperboundMulti', 'GMP::Column::Unfreeze','GMP::Column::UnfreezeMulti','GMP::Instance::AddIntegerEliminationRows', 'GMP::Instance::CalculateSubGradient','GMP::Instance::Copy','GMP::Instance::CreateFeasibility','GMP::Instance::CreateDual', 'GMP::Instance::CreateMasterMip','GMP::Instance::CreatePresolved','GMP::SolverSession::CreateProgressCategory', 'GMP::Instance::CreateProgressCategory','GMP::Instance::CreateSolverSession','GMP::Stochastic::CreateBendersRootproblem', 'GMP::Instance::Delete','GMP::Instance::DeleteIntegerEliminationRows','GMP::Instance::DeleteSolverSession', 'GMP::Instance::FindApproximatelyFeasibleSolution','GMP::Instance::FixColumns','GMP::Instance::Generate', 'GMP::Instance::GenerateRobustCounterpart','GMP::Instance::GenerateStochasticProgram', 'GMP::SolverSession::GetCallbackInterruptStatus','GMP::SolverSession::WaitForCompletion', 'GMP::SolverSession::WaitForSingleCompletion','GMP::SolverSession::ExecutionStatus','GMP::Instance::GetColumnNumbers', 'GMP::Instance::GetDirection','GMP::Instance::GetBestBound','GMP::Instance::GetMathematicalProgrammingType', 'GMP::Instance::GetMemoryUsed','GMP::Instance::GetNumberOfColumns','GMP::Instance::GetNumberOfIndicatorRows', 'GMP::Instance::GetNumberOfIntegerColumns','GMP::Instance::GetNumberOfNonlinearColumns', 'GMP::Instance::GetNumberOfNonlinearNonzeros','GMP::Instance::GetNumberOfNonlinearRows','GMP::Instance::GetNumberOfNonzeros', 'GMP::Instance::GetNumberOfRows','GMP::Instance::GetNumberOfSOS1Rows','GMP::Instance::GetNumberOfSOS2Rows', 'GMP::Instance::GetObjective','GMP::Instance::GetOptionValue','GMP::Instance::GetRowNumbers', 'GMP::Instance::GetObjectiveColumnNumber','GMP::Instance::GetObjectiveRowNumber','GMP::Instance::GetSolver', 'GMP::Instance::GetSymbolicMathematicalProgram','GMP::Instance::MemoryStatistics','GMP::Instance::Rename', 'GMP::Instance::SetCallbackAddCut','GMP::Instance::SetCallbackAddLazyConstraint','GMP::Instance::SetCallbackBranch', 'GMP::Instance::SetCallbackHeuristic','GMP::Instance::SetCallbackIncumbent','GMP::Instance::SetCallbackIterations', 'GMP::Instance::SetCallbackNewIncumbent','GMP::Instance::SetCallbackStatusChange','GMP::Instance::SetCallbackTime', 'GMP::Instance::SetCutoff','GMP::Instance::SetDirection','GMP::Instance::SetMathematicalProgrammingType','GMP::Instance::SetSolver', 'GMP::Instance::SetStartingPointSelection','GMP::Instance::Solve','GMP::Stochastic::GetObjectiveBound', 'GMP::Stochastic::GetRelativeWeight','GMP::Stochastic::GetRepresentativeScenario','GMP::Stochastic::UpdateBendersSubproblem', 'GMP::Linearization::Add','GMP::Linearization::AddSingle','GMP::Linearization::Delete','GMP::Linearization::GetDeviation', 'GMP::Linearization::GetDeviationBound','GMP::Linearization::GetLagrangeMultiplier','GMP::Linearization::GetType', 'GMP::Linearization::GetWeight','GMP::Linearization::RemoveDeviation','GMP::Linearization::SetDeviationBound', 'GMP::Linearization::SetType','GMP::Linearization::SetWeight','GMP::ProgressWindow::DeleteCategory', 'GMP::ProgressWindow::DisplayLine','GMP::ProgressWindow::DisplayProgramStatus','GMP::ProgressWindow::DisplaySolver', 'GMP::ProgressWindow::DisplaySolverStatus','GMP::ProgressWindow::FreezeLine','GMP::ProgressWindow::UnfreezeLine', 'GMP::ProgressWindow::Transfer','GMP::QuadraticCoefficient::Get','GMP::QuadraticCoefficient::Set','GMP::Row::Activate', 'GMP::Stochastic::AddBendersFeasibilityCut','GMP::Stochastic::AddBendersOptimalityCut', 'GMP::Stochastic::BendersFindFeasibilityReference','GMP::Stochastic::MergeSolution','GMP::Row::Add','GMP::Row::Deactivate', 'GMP::Row::Delete','GMP::Row::DeleteIndicatorCondition','GMP::Row::Generate','GMP::Row::GetConvex','GMP::Row::GetIndicatorColumn', 'GMP::Row::GetIndicatorCondition','GMP::Row::GetLeftHandSide','GMP::Row::GetName','GMP::Row::GetRelaxationOnly', 'GMP::Row::GetRightHandSide','GMP::Row::GetScale','GMP::Row::GetStatus','GMP::Row::GetType','GMP::Row::SetConvex', 'GMP::Row::SetPoolType','GMP::Row::SetPoolTypeMulti','GMP::Row::SetIndicatorCondition','GMP::Row::SetLeftHandSide', 'GMP::Row::SetRelaxationOnly','GMP::Row::SetRightHandSide','GMP::Row::SetRightHandSideMulti','GMP::Row::SetType', 'GMP::Solution::Check','GMP::Solution::ConstraintListing','GMP::Solution::Copy','GMP::Solution::Count','GMP::Solution::Delete', 'GMP::Solution::DeleteAll','GMP::Solution::GetColumnValue','GMP::Solution::GetTimeUsed','GMP::Solution::GetDistance', 'GMP::Solution::GetFirstOrderDerivative','GMP::Solution::GetIterationsUsed','GMP::Solution::GetNodesUsed', 'GMP::Solution::GetBestBound','GMP::Solution::GetMemoryUsed','GMP::Solution::GetObjective','GMP::Solution::GetPenalizedObjective', 'GMP::Solution::GetProgramStatus','GMP::Solution::GetRowValue','GMP::Solution::GetSolutionsSet','GMP::Solution::GetSolverStatus', 'GMP::Solution::IsDualDegenerated','GMP::Solution::IsInteger','GMP::Solution::IsPrimalDegenerated','GMP::Solution::SetMIPStartFlag', 'GMP::Solution::Move','GMP::Solution::RandomlyGenerate','GMP::Solution::RetrieveFromModel', 'GMP::Solution::RetrieveFromSolverSession','GMP::Solution::SendToModel','GMP::Solution::SendToModelSelection', 'GMP::Solution::SendToSolverSession','GMP::Solution::SetIterationCount','GMP::Solution::SetColumnValue', 'GMP::Solution::SetRowValue','GMP::Solution::SetObjective','GMP::Solution::SetProgramStatus','GMP::Solution::SetSolverStatus', 'GMP::Solution::UpdatePenaltyWeights','GMP::Solution::ConstructMean','GMP::SolverSession::AsynchronousExecute', 'GMP::SolverSession::Execute','GMP::SolverSession::Interrupt','GMP::SolverSession::AddLinearization', 'GMP::SolverSession::AddBendersOptimalityCut','GMP::SolverSession::AddBendersFeasibilityCut', 'GMP::SolverSession::GenerateBranchLowerBound','GMP::SolverSession::GenerateBranchUpperBound', 'GMP::SolverSession::GenerateBranchRow','GMP::SolverSession::GenerateCut','GMP::SolverSession::GenerateBinaryEliminationRow', 'GMP::SolverSession::GetCandidateObjective','GMP::SolverSession::GetTimeUsed','GMP::SolverSession::GetHost', 'GMP::SolverSession::GetInstance','GMP::SolverSession::GetIterationsUsed','GMP::SolverSession::GetNodesLeft', 'GMP::SolverSession::GetNodesUsed','GMP::SolverSession::GetNodeNumber','GMP::SolverSession::GetNodeObjective', 'GMP::SolverSession::GetNumberOfBranchNodes','GMP::SolverSession::GetBestBound','GMP::SolverSession::GetMemoryUsed', 'GMP::SolverSession::GetObjective','GMP::SolverSession::GetOptionValue','GMP::SolverSession::GetProgramStatus', 'GMP::SolverSession::GetSolver','GMP::SolverSession::GetSolverStatus','GMP::SolverSession::RejectIncumbent','GMP::Event::Create', 'GMP::Event::Delete','GMP::Event::Reset','GMP::Event::Set','GMP::SolverSession::SetObjective','GMP::SolverSession::SetOptionValue', 'GMP::Instance::SetTimeLimit','GMP::Instance::SetIterationLimit','GMP::Instance::SetMemoryLimit','GMP::Instance::SetOptionValue', 'GMP::Tuning::SolveSingleMPS','GMP::Tuning::TuneMultipleMPS','GMP::Tuning::TuneSingleGMP','GMP::Solver::InitializeEnvironment', 'GMP::Solver::FreeEnvironment','GMP::Solver::GetAsynchronousSessionsLimit','GMP::Robust::EvaluateAdjustableVariables', 'GMP::Benders::CreateMasterProblem','GMP::Benders::CreateSubProblem','GMP::Benders::UpdateSubProblem', 'GMP::Benders::AddOptimalityCut','GMP::Benders::AddFeasibilityCut','GMP::Column::SetDecomposition', 'GMP::Column::SetDecompositionMulti','GenerateXML','GetDatasourceProperty','ReadGeneratedXML','ReadXML','ReferencedIdentifiers', 'WriteXML','IdentifierAttributes','IdentifierDimension','IdentifierElementRange','IsRuntimeIdentifier','IdentifierMemory', 'IdentifierMemoryStatistics','IdentifierText','IdentifierType','IdentifierUnit','SaveDatabaseStructure','ScalarValue', 'SectionIdentifiers','SubRange','MemoryInUse','CommitTransaction','RollbackTransaction','MemoryStatistics','me::AllowedAttribute', 'me::ChangeType','me::ChangeTypeAllowed','me::Children','me::ChildTypeAllowed','me::Compile','me::Create','me::CreateLibrary', 'me::Delete','me::ExportNode','me::GetAttribute','me::ImportLibrary','me::ImportNode','me::IsRunnable','me::Move','me::Parent', 'me::Rename','me::SetAnnotation','me::SetAttribute','MomentToString','MomentToTimeSlot','OptionGetValue','OptionGetKeywords', 'OptionGetDefaultString','OptionGetString','OptionSetString','OptionSetValue','PeriodToString','ProfilerContinue','ProfilerPause', 'ProfilerRestart','RestoreInactiveElements','RetrieveCurrentVariableValues','SetAddRecursive','SetElementAdd','SetElementRename', 'SQLColumnData','SQLCreateConnectionString','SQLDriverName','SQLNumberOfColumns','SQLNumberOfDrivers','SQLNumberOfTables', 'SQLNumberOfViews','SQLTableName','SQLViewName','StartTransaction','StringToElement','StringToMoment','StringToTimeSlot', 'TestDatabaseColumn','TestDatabaseTable','TestDataSource','TestDate','TimeslotCharacteristic','TimeslotToMoment','TimeslotToString', 'TimeZoneOffset','VariableConstraints','Execute','GetAnnotationValues','PageOpen','PageOpenSingle','PageClose','PageGetActive', 'PageSetFocus','PageGetFocus','PageSetCursor','PageRefreshAll','PageGetChild','PageGetParent','PageGetNext','PageGetPrevious', 'PageGetNextInTreeWalk','PageGetUsedIdentifiers','PageGetTitle','PageGetAll','PageCopyTableToClipboard','PageCopyTableToExcel', 'PageCopyTableToSpreadsheet','PrintPage','PrintPageCount','PrintStartReport','PrintEndReport','PrinterSetupDialog', 'PrinterGetCurrentName','PivotTableReloadState','PivotTableSaveState','PivotTableDeleteState','FileSelect','FileSelectNew', 'FileDelete','FileExists','FileCopy','FileMove','FileView','FileEdit','FilePrint','FileTime','FileTouch','FileAppend','FileGetSize', 'DirectorySelect','DirectoryCreate','DirectoryDelete','DirectoryExists','DirectoryCopy','DirectoryMove','DirectoryGetCurrent', 'DirectoryOfLibraryProject','DialogProgress','DialogMessage','DialogError','StatusMessage','DialogAsk','DialogGetString', 'DialogGetDate','DialogGetNumber','DialogGetElement','DialogGetElementByText','DialogGetElementByData','DialogGetPassword', 'DialogGetColor','CaseNew','CaseFind','CaseCreate','CaseLoadCurrent','CaseMerge','CaseLoadIntoCurrent','CaseSelect','CaseSelectNew', 'CaseSetCurrent','CaseSave','CaseSaveAll','CaseSaveAs','CaseSelectMultiple','CaseGetChangedStatus','CaseSetChangedStatus', 'CaseDelete','CaseGetType','CaseGetDatasetReference','CaseWriteToSingleFile','CaseReadFromSingleFile','DatasetNew','DatasetFind', 'DatasetCreate','DatasetLoadCurrent','DatasetMerge','DatasetLoadIntoCurrent','DatasetSelect','DatasetSelectNew','DatasetSetCurrent', 'DatasetSave','DatasetSaveAll','DatasetSaveAs','DatasetGetChangedStatus','DatasetSetChangedStatus','DatasetDelete', 'DatasetGetCategory','DataFileGetName','DataFileGetAcronym','DataFileSetAcronym','DataFileGetComment','DataFileSetComment', 'DataFileGetPath','DataFileGetTime','DataFileGetOwner','DataFileGetGroup','DataFileReadPermitted','DataFileWritePermitted', 'DataFileExists','DataFileCopy','DataCategoryContents','CaseTypeContents','CaseTypeCategories','OpenDocument', 'TestInternetConnection','GeoFindCoordinates','ShowHelpTopic','Delay','ScheduleAt','ExitAimms','SessionArgument', 'SessionHasVisibleGUI','ProjectDeveloperMode','DebuggerBreakpoint','ShowProgressWindow','ShowMessageWindow','SolverGetControl', 'SolverReleaseControl','ProfilerStart','IdentifierGetUsedInformation','IdentifierShowAttributes','IdentifierShowTreeLocation', 'DataManagerImport','DataManagerExport','DataManagerFileNew','DataManagerFileOpen','DataManagerFileGetCurrent','DataImport220', 'DataManagementExit','CaseFileSave','CaseFileLoad','CaseFileMerge','CaseFileGetContentType','CaseFileSectionSave', 'CaseFileSectionLoad','CaseFileSectionMerge','CaseFileSectionGetContentType','CaseFileSectionExists','CaseFileSectionRemove', 'CaseFileURLtoElement','CaseFileSetCurrent','CaseDialogConfirmAndSave','CaseCommandLoadAsActive','CaseCommandMergeIntoActive', 'CaseCommandLoadIntoActive','CaseCommandSave','CaseCommandSaveAs','CaseCommandNew','CaseDialogSelectMultiple', 'CaseDialogSelectForLoad','CaseDialogSelectForSave','DataChangeMonitorCreate','DataChangeMonitorReset', 'DataChangeMonitorHasChanged','DataChangeMonitorDelete','SecurityGetUsers','SecurityGetGroups','UserColorAdd','UserColorDelete', 'UserColorGetRGB','UserColorModify','LicenseNumber','LicenseType','LicenseStartDate','LicenseExpirationDate', 'LicenseMaintenanceExpirationDate','AimmsRevisionString','HistogramCreate','HistogramDelete','HistogramSetDomain', 'HistogramAddObservation','HistogramAddObservations','HistogramGetFrequencies','HistogramGetBounds','HistogramGetObservationCount', 'HistogramGetAverage','HistogramGetDeviation','HistogramGetSkewness','HistogramGetKurtosis','DateDifferenceDays', 'DateDifferenceYearFraction','PriceFractional','PriceDecimal','RateEffective','RateNominal','DepreciationLinearLife', 'DepreciationLinearRate','DepreciationNonLinearSumOfYear','DepreciationNonLinearLife','DepreciationNonLinearFactor', 'DepreciationNonLinearRate','DepreciationSum','InvestmentConstantPresentValue','InvestmentConstantFutureValue', 'InvestmentConstantPeriodicPayment','InvestmentConstantInterestPayment','InvestmentConstantPrincipalPayment', 'InvestmentConstantCumulativePrincipalPayment','InvestmentConstantCumulativeInterestPayment','InvestmentConstantNumberPeriods', 'InvestmentConstantRateAll','InvestmentConstantRate','InvestmentVariablePresentValue','InvestmentVariablePresentValueInperiodic', 'InvestmentSingleFutureValue','InvestmentVariableInternalRateReturnAll','InvestmentVariableInternalRateReturn', 'InvestmentVariableInternalRateReturnInperiodicAll','InvestmentVariableInternalRateReturnInperiodic', 'InvestmentVariableInternalRateReturnModified','SecurityDiscountedPrice','SecurityDiscountedRedemption','SecurityDiscountedYield', 'SecurityDiscountedRate','TreasuryBillPrice','TreasuryBillYield','TreasuryBillBondEquivalent','SecurityMaturityPrice', 'SecurityMaturityCouponRate','SecurityMaturityYield','SecurityMaturityAccruedInterest','SecurityCouponNumber', 'SecurityCouponPreviousDate','SecurityCouponNextDate','SecurityCouponDays','SecurityCouponDaysPreSettlement', 'SecurityCouponDaysPostSettlement','SecurityPeriodicPrice','SecurityPeriodicRedemption','SecurityPeriodicCouponRate', 'SecurityPeriodicYieldAll','SecurityPeriodicYield','SecurityPeriodicAccruedInterest','SecurityPeriodicDuration', 'SecurityPeriodicDurationModified','Abs','AtomicUnit','Ceil','Character','CharacterNumber','Cube','Degrees','Div','Exp','Floor', 'Log','Log10','Mapval','Max','Min','Mod','Power','Radians','Round','Sign','Sqr','Sqrt','StringCapitalize','StringLength', 'StringToLower','StringToUnit','StringToUpper','SubString','Trunc','Binomial','NegativeBinomial','Poisson','Geometric', 'HyperGeometric','Uniform','Normal','LogNormal','Triangular','Exponential','Weibull','Beta','Gamma','Logistic','Pareto', 'ExtremeValue','Precision','Factorial','Combination','Permutation','Errorf','Cos','Sin','Tan','ArcCos','ArcSin','ArcTan','Cosh', 'Sinh','Tanh','ArcCosh','ArcSinh','ArcTanh' ), prefix=r'\b(?i)', suffix=r'\b'), Name.Builtin),
            
            #Highlights mathematical operators
            (r'(\+|\-|\*|/|\*\*|=|<=|>=|==|\||\^|<|>|\!|\.\.|:=|\&|\!=|<<|>>|;)',
             Operator),
            
            #For AMS files, matches all function arguments
            #(r'(\w+\s+)(:)([^=:].*,|[^=:].*;|,|;|\n.*})', bygroups(Name.Argument,Operator,Text)),
            
            #Identifiers prefix match: if ANYTHING starts with a EP_ or P_ or ... it is parameter (green) or element parameter (blue), etc.
            (r'(?i)(\bP_\w+\b)', bygroups(Name.Parameter)),
            (r'(?i)(\bP01_\w+\b)', bygroups(Name.Parameter)),
            (r'(?i)(\bEP_\w+\b)', bygroups(Name.ElementParameter)),
            (r'(?i)(\bS_\w+\b)', bygroups(Name.Set)),
            (r'(?i)(\bCal_\w+\b)', bygroups(Name.Set)),
            (r'(?i)(\bSP_\w+\b)', bygroups(Name.StringParameter)),
            (r'(?i)(\bV_\w+\b)', bygroups(Name.Variable)),
            (r'(?i)(\bV01_\w+\b)', bygroups(Name.Variable)),
            (r'(?i)(\bEV_\w+\b)', bygroups(Name.Variable)),
            (r'(?i)(\bC_\w+\b)', bygroups(Name.Constraint)),
            (r'(?i)(\bMP_\w+\b)', bygroups(Name.MathematicalProgram)),
            (r'(?i)(\bDBT_\w+\b)', bygroups(Name.DatabaseTable)),
            (r'(?i)(\bPR_\w+\b)', bygroups(Name.Variable)),
            (r'(?i)(\bCNV_\w+\b)', bygroups(Name.Convention)),
            (r'(?i)(\bI_\w+\b)', bygroups(Name.Index)),
            
            
            #Clean every unmatched # character, after everything is matched
            (r'#',Text),
            (r'(\w+|(\.(?!\.)))', Text)
        ]
        
    }

        
    def get_tokens_unprocessed(self,text):
        
        # for AMS files: catch any identifier declaration, and highlight every reference in the rest of the file. In other words, every user defined identifier is triggered :) Because I can.
        
        m = id_re.findall(text)
        # Ok, we found all matches from the big identifiers list. thus we end up with a list like this: 
        # m = [first_match, second_match, ...] and nth_match = (id_type,id_name,id_operator) = ('Parameter', 'OD', ';')
        
        id_nametype = {}
        
        for i in m:
        
            id_nametype[i[1]] = i[0]
        
                
        #print "I'm in get_tokens_unprocessed"
        
            
        for index, token, value in RegexLexer.get_tokens_unprocessed(self, text):
            
            # if the item is part of the declared (detected) identifiers, attach the appropriate token, thanks to the switcher :)
            if any(item == value for item in id_nametype.keys()): 
                yield index, switcher(id_nametype[value]), value
            
            # if the item is not detected as an function argument and is part of the Identifier type list, attach a 'kd' token 
            elif (not token is Name.Argument and any(item == value for item in id_nametype.values())): 
                yield index, Keyword.Declaration, value

            else:
                yield index, token ,value              
