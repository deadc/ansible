#!/usr/bin/env bash

ROLE=$1

if [ ! -z ${ROLE} ] ; then
  echo "RUN: Applying role tag ${ROLE}"
  ansible-playbook -i localhost, tests.yml --diff --connection=local --tags ${ROLE}
  echo "RUN: Generating goss template"
  ansible -i localhost, --connection=local all -m setup --tree . &>/dev/null
  echo "RUN: Running tests"
  goss --vars localhost -g roles/${ROLE}/goss.yaml validate
else
  echo "RUN: Checking syntax.."
  ansible-playbook -i localhost, tests.yml --syntax-check --connection=local
  echo "RUN: Applying roles configured at tests.yml"
  ansible-playbook -i localhost, tests.yml --diff --connection=local
  echo "RUN: Generating goss template"
  ansible -i localhost, --connection=local all -m setup --tree . &>/dev/null
  echo "RUN: Running tests"
  goss --vars localhost -g goss.yml validate
fi
