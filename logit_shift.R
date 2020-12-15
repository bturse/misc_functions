#' logit_shift
#' adjust modeled logistic probability to match forecast aggregate
#' @param orig_prob  numeric vector of probabilities to adjust
#' @param c          decimal, values to shift logits by to recalculate adjusted
#'   probabilities
#' @return numeric vector of adjusted probabilities
logit_shift <- function(orig_probs, c){
  # log_odds: converted probability to logits
  # this is neessary to ensure all adjsuted probabilities are between 0-1
  log_odds <- log(orig_probs/(1-orig_probs))
  # adj_log_odds: incremented logits
  adj_log_odds <- log_odds + c
  # convert adj_log_odds back to probability
  orig_probs <- exp(adj_log_odds)/(exp(adj_log_odds)+1)
}
